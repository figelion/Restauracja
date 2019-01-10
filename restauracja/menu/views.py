# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.template import loader

from .models import PeriodicMenu
from .models import Place
from .models import Comment
from .models import Dishes

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def index(request):
    place_list = Place.objects.order_by('id')
    context = {'place_list': place_list}
    return render(request, 'menu/index.html', context)

def detail(request, place_id):

    menu_list = PeriodicMenu.objects.filter(PeriodicMenu.place == place_id)
    comments_list = Comment.objects.filter(Comment.place == place_id)
    context = {'menu_list': menu_list,
               'comments_list': comments_list
               }

    return render(request, 'menu/index.html', context)

def dishes(request, periodicMenu_id):
    # try:
    #     menu = PeriodicMenu.objects.get(pk=periodicMenu_id)
    # except PeriodicMenu.DoesNotExist:
    #     raise Http404("Menu does not exist")
    # return render(request, 'menu/detail.html', {'menu':menu})
    menu = get_object_or_404(PeriodicMenu, pk=periodicMenu_id)
    return render(request, 'menu/dishes.html', {'menu': menu})


