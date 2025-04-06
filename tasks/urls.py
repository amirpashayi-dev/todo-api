from django.urls import path
from . import views

urlpatterns = [
    path('', views.TasksAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TasksDetailAPIView.as_view(), name='task-detail'),
]