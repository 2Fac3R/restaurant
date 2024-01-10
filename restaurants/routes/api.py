"""API Routes."""

# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework import routers

# Views
from ..views.api import RestaurantApiView as restaurant_views


# API Routing
router = routers.DefaultRouter()
router.register(r'restaurants', restaurant_views.RestaurantViewSet, basename='restaurants')

urlpatterns = [
    # Routes
    path('', include(router.urls)),
    # Auth
    path('api-auth/', include('rest_framework.urls')),
]
