from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the menu index.")

def detail(request, periodicMenu_id):
    return HttpResponse("Tou are looking at menu %s"% periodicMenu_id)

#TODO  do usunięcia z widoków - klient widzi tylko dane menu
def dish(request , dish_id):
    return HttpResponse("Tou are looking at dish %s" % dish_id)

