from django.db import models

# Create your models here.

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
    #dish = models.ManyToManyField(Dishes, blank=True, null=True)

    def __str__(self):
        return self.name



