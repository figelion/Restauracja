from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.index, name='places'),
    path('<int:place_id>/', views.detail, name='detail'),
    path('^<int:periodicMenu_id>/', views.dishes, name='dishes'),
]