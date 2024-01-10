"""Restaurant API Views."""

# Django Rest Framework
from rest_framework import viewsets

# Restaurant App
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Restaurants to be viewed or edited.
    """
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer
