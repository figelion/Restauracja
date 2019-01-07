from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.index, name='places'),
    path('<int:periodicMenu_id>/', views.detail, name='detail'),
    path('<int:dish_id>/', views.dish, name='dish'),
]