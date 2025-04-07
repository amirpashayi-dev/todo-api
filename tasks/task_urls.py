from django.urls import path
from .views import TasksAPIView, TasksDetailAPIView, MarkTaskAsDoneAPIView

urlpatterns = [
    path('', TasksAPIView.as_view(), name='task-list-create'),
    path('<int:pk>/', TasksDetailAPIView.as_view(), name='task-detail'),
    path('<int:pk>/done/', MarkTaskAsDoneAPIView.as_view(), name='mark-as-done'),
]
