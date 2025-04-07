from django.urls import path
from .views import TasksAPIView, TasksDetailAPIView

urlpatterns = [
    path('', TasksAPIView.as_view(), name='task-list-create'),
    path('<int:pk>/', TasksDetailAPIView.as_view(), name='task-detail'),
]
