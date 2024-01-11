"""Tests for Restaurant views."""

# Django
from django.urls import reverse

# Testing
from rest_framework.test import APITestCase
from rest_framework import status

# Restaurant app
from ..models import Restaurant


class RestaurantViewSetTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('restaurants-list')

    def test_there_is_no_content(self):
        """There is no content yet."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, [])

    def test_there_is_content(self):
        """There is content."""
        restaurant = Restaurant.objects.create(lat=40.7, lng=-74.0, rating=4)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, restaurant)

    def test_create(self):
        """POST: Create a new restaurant."""
        data = {
            "id": "71795f1x-4xa0-4ex7-b925-5b906711329x",
            "rating": 4,
            "name": "EDT Restaurant",
            "site": "https://exploration.mx/",
            "email": "email@exploration.mx",
            "phone": "138272475",
            "street": "Terrazasside Urbanización",
            "city": "Ciudad de México",
            "state": "Estado de México",
            "lat": 19.4386824334767,
            "lng": -99.1289113955692
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.get().name, 'EDT Restaurant')

    def test_read(self):
        """GET: Get a restaurant by ID."""
        restaurant = Restaurant.objects.create(
            id="71795f1x-4xa0-4ex7-b925-5b906711329x", lat=40.7, lng=-74.0, rating=4)
        response = self.client.get(
            reverse('restaurants-detail', args=(restaurant.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, restaurant)

    def test_update(self):
        """PUT: Update a restaurant."""
        restaurant = Restaurant.objects.create(
            id="71795f1x-4xa0-4ex7-b925-5b906711329x", lat=40.7, lng=-74.0, rating=4)
        data = {
            "id": "71795f1x-4xa0-4ex7-b925-5b906711329x",
            "rating": 4,
            "name": "EDT Excelent Restaurant",
            "site": "https://exploration.mx/",
            "email": "soporte@exploration.mx",
            "phone": "138272475",
            "street": "Terrazasside Urbanización",
            "city": "Ciudad de México",
            "state": "Estado de México",
            "lat": 19.4386824334767,
            "lng": -99.1289113955692
        }
        response = self.client.put(
            reverse('restaurants-detail', args=(restaurant.id,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.get().name,
                         'EDT Excelent Restaurant')

    def test_partial_update(self):
        """PATCH: Update a restaurant field, rating."""
        restaurant = Restaurant.objects.create(
            id="71795f1x-4xa0-4ex7-b925-5b906711329x", lat=40.7, lng=-74.0, rating=4)
        new_data = {
            "rating": 3,
        }
        response = self.client.patch(
            reverse('restaurants-detail', args=(restaurant.id,)), new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.get().rating, 3)

    def test_delete(self):
        """DELETE: Delete a restaurant."""
        restaurant = Restaurant.objects.create(
            id="71795f1x-4xa0-4ex7-b925-5b906711329x", lat=40.7, lng=-74.0, rating=4)
        response = self.client.delete(
            reverse('restaurants-detail', args=(restaurant.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


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
        expected_response = {
            'count': 3,
            'avg': 4.0,
            'std': 0.816496580927726,
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_get_restaurants_statistics_no_params(self):
        """Test the API endpoint without parameters."""
        response = self.client.get(self.url)
        expected_response = {
            "count": 0,
            "avg": None,
            "std": None
        }
        self.assertEqual(response.data, expected_response)
