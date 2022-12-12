from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.conf import settings


# Setting the house categoryes and to
# create a house with a sertian number of beds


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
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'


# Making a booking for a user for a sertian amount of time


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.house} from {self.check_in} to {self.check_out}'
