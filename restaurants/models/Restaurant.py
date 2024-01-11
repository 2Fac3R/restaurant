"""Model: Restaurant"""

# Django
from django.urls import reverse

# GeoDjango
from django.db import models


class Restaurant(models.Model):
    """Model representing a Restaurant."""

    RATING_CHOICES = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    ]

    id = models.CharField(primary_key=True, max_length=255)
    rating = models.IntegerField(choices=RATING_CHOICES)
    name = models.TextField()
    site = models.TextField()
    email = models.EmailField()
    phone = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular Restaurant instance."""
        return reverse('restaurant-detail', args=[str(self.id)])
