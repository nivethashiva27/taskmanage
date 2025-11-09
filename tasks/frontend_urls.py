from django.urls import path
from . import frontend_views

urlpatterns = [
    path('', frontend_views.tasks_frontend, name='tasks-frontend'),
]
