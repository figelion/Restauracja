from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.template import loader

from .models import PeriodicMenu
from .models import Dishes

# Create your views here.

from django.http import HttpResponse


def index(request):
    menu_list = PeriodicMenu.objects.order_by('id')
    context = {'menu_list': menu_list}
    return render(request, 'menu/index.html', context)

def detail(request, periodicMenu_id):
    try:
        menu = PeriodicMenu.objects.get(pk=periodicMenu_id)
    except PeriodicMenu.DoesNotExist:
        raise Http404("Menu does not exist")
    return render(request, 'menu/detail.html', {'menu':menu})
    menu = get_object_or_404(PeriodicMenu, pk=periodicMenu_id)
    return render(request, 'menu/detail.html', {'question':question})

#TODO  do usunięcia z widoków - klient widzi tylko dane menu
def dish(request , dish_id):
    return HttpResponse("Tou are looking at dish %s" % dish_id)

