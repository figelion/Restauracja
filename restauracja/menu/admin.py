from django.contrib import admin
from .models import Dishes
from .models import PeriodicMenu

# Register your models here.
admin.site.register(Dishes)
admin.site.register(PeriodicMenu)

