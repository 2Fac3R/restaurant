"""URL configuration for restaurant_project project."""

# Django
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


# Routes
urlpatterns = [
    # Restaurants
    path('restaurants/', include('restaurants.urls')),
    # Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
