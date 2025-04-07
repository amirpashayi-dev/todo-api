from django.urls import path
from . import views

urlpatterns = [
    path('', views.TasksAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TasksDetailAPIView.as_view(), name='task-detail'),
    path('categories/', views.CategoryAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='category-detail'),


]