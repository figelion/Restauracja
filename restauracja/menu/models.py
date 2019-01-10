from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Place (models.Model):
    town = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.town

class Dishes(models.Model):
    name = models.CharField(max_length=200)                                              #nazwa
    description = models.CharField(max_length=500)                                                     #opis - z czego jest
    price = models.FloatField()                                                          #cena
    type = models.CharField(max_length=200)                                                            #Jaki typ potrawy

    def __str__(self):
        return self.name

class PeriodicMenu (models.Model):
    name = models.CharField(max_length=200, default="Menu przykładowe")
    period = models.CharField(max_length=200)                                       #Okres w jakim obowiązuje np. Zima
    dish = models.ManyToManyField(Dishes, blank=True, null=True)
    place = models.ManyToManyField(Place, null=True)

    def __str__(self):
        return self.name

class Comment (models.Model):
    comment_text = models.CharField(max_length=500)
    author = models.ForeignKey (User, on_delete=models.CASCADE)
    place = models.ForeignKey (Place, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.place.town
