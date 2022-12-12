from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone


class House(models.Model):
    HOUSE_CATEGORIES = (
        ('BAS', 'BASIC'),
        ('LUX', 'LUXURIUS'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=HOUSE_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people.'
