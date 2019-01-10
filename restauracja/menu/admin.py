from django.contrib import admin
from .models import Dishes
from .models import PeriodicMenu
from .models import Place
from .models import Comment

# Register your models here.
admin.site.register(Dishes)
admin.site.register(PeriodicMenu)
admin.site.register(Place)
admin.site.register(Comment)
