"""Restaurant Serializer."""

# Django Rest Framework
from rest_framework import serializers

# Restaurants app
from restaurants.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
