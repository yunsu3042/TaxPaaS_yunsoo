from django.db import models
from functions import RandomFileName


class Car(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(
        upload_to=RandomFileName('cars/volvo'),
        blank=True
    )
