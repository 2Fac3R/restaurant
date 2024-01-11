"""Tests for Restaurant views."""

# Django
from django.urls import reverse

# Testing
from rest_framework.test import APITestCase
from rest_framework import status

# Restaurant app
from ..models import Restaurant


class RestaurantStatisticsViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('restaurant-statistics')
        self.restaurant1 = Restaurant.objects.create(
            id="adb77425-2c3f-435c-8391-021b40010b0a", lat=40.7, lng=-74.0, rating=4)
        self.restaurant2 = Restaurant.objects.create(
            id="bdb77425-2c3f-435c-8391-021b40010b0b", lat=40.8, lng=-74.1, rating=3)
        self.restaurant3 = Restaurant.objects.create(
            id="cdb77425-2c3f-435c-8391-021b40010b0c", lat=41.0, lng=-73.9, rating=5)

    def test_get_restaurants_statistics(self):
        """Parameters for the circle centered at (40.9, -74.0) with radius 10 kms."""
        params = {'latitude': 40.9, 'longitude': -74.0, 'radius': 10000}

        response = self.client.get(self.url, params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the response content
        expected_response = {
            'count': 3,
            'avg': 4.0,
            'std': 0.816496580927726,
        }
        self.assertEqual(response.data, expected_response)

    def test_get_restaurants_statistics_no_params(self):
        """Test the API endpoint without parameters."""
        response = self.client.get(self.url)

        # Check the response content
        expected_response = {
            "count": 0,
            "avg": None,
            "std": None
        }
        self.assertEqual(response.data, expected_response)
