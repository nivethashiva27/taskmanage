from django.urls import path
from .views import TaskListCreateView, TaskDetailView, mark_task_completed

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', mark_task_completed, name='task-complete'),
]
