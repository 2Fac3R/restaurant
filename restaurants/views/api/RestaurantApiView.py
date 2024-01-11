"""Restaurant API Views."""

# Django
from django.db.models import Avg, StdDev

# Django Rest Framework
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# Restaurant App
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Restaurants to be viewed or edited.
    """
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer


class RestaurantStatisticsView(APIView):
    def get(self, request):
        """
        It receives a latitude and a longitude as parameters, which correspond to the center of a circle,
        and a third parameter that corresponds to a radius in METERS.

        Args:
            request (HttpRequest): latitude, longitude, radius (float, float, float).

        Returns:
            {
                count: Count of restaurants that fall inside the circle with center [x,y] and radius z,
                avg: Average rating of restaurant inside the circle,
                std: Standard deviation of rating of restaurants inside the circle
            }
        """
        # One degree of latitude equals 111.11 kms.
        DEGREES_TO_KILOMETERS = 111

        # Get parameters from the request
        latitude = float(request.query_params.get('latitude', 0))
        longitude = float(request.query_params.get('longitude', 0))
        radius = float(request.query_params.get('radius', 0))

        # Define the rectangular bounds
        min_lat, max_lat = latitude - \
            (radius / DEGREES_TO_KILOMETERS), latitude + \
            (radius / DEGREES_TO_KILOMETERS)
        min_lng, max_lng = longitude - \
            (radius / DEGREES_TO_KILOMETERS), longitude + \
            (radius / DEGREES_TO_KILOMETERS)

        # Filter restaurants inside the specified rectangle
        restaurants = Restaurant.objects.filter(
            lat__isnull=False,
            lng__isnull=False,
            lat__range=(min_lat, max_lat),
            lng__range=(min_lng, max_lng),
        )

        # Calculate count, average rating, and standard deviation
        count = restaurants.count()
        avg_rating = restaurants.aggregate(
            avg_rating=Avg('rating'))['avg_rating']
        std_dev_rating = restaurants.aggregate(
            std_dev_rating=StdDev('rating'))['std_dev_rating']

        # Create the response JSON
        response_data = {
            'count': count,
            'avg': avg_rating,
            'std': std_dev_rating,
        }

        return Response(response_data)
