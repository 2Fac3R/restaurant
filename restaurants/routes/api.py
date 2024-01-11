"""API Routes."""

# Django
from django.urls import path, include, re_path

# Django Rest Framework
from rest_framework import routers

# Config
from ..config.api import schema_view

# Views
from ..views.api import RestaurantApiView as restaurant_views


# API Routing
router = routers.DefaultRouter()
router.register(
    r'restaurants', restaurant_views.RestaurantViewSet, basename='restaurants')

urlpatterns = [
    # Routes
    path('', include(router.urls)),
    path('statistics', restaurant_views.RestaurantStatisticsView.as_view(),
         name='restaurant-statistics'),
    # API Documentation
    re_path(
        'swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    # Auth
    path('api-auth/', include('rest_framework.urls')),
]
