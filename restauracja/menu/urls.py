from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dishes_id>/', views.detail, name='detail'),
    path('<int:periodicMenu_id>/', views.menu, name = 'menu')
]