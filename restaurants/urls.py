"""Restaurants URLs Configuration."""

# Django
from django.urls import path, include

# Routes
from .routes.api import urlpatterns as api


urlpatterns = [
    # API
    path('', include(api)),
]
