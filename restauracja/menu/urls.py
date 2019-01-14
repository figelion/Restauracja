from django.urls import path
from .views import (
    CommentListView,
    CommentDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)
from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.index, name='places'),
    path('<int:place_id>/', CommentListView.as_view(), name='detail'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('comment/new/<int:place_id>', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('^<int:periodicMenu_id>/', views.dishes, name='dishes'),
]