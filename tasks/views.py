from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    """
    GET: list tasks; supports ?status=PENDING or ?status=COMPLETED
    POST: create a task
    """
    serializer_class = TaskSerializer

    def get_queryset(self):
        qs = Task.objects.all().order_by('-created_at')
        status_param = self.request.GET.get('status')
        if status_param:
            status_param = status_param.upper()
            if status_param in [Task.STATUS_PENDING, Task.STATUS_COMPLETED]:
                qs = qs.filter(status=status_param)
        return qs

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@api_view(['POST'])
def mark_task_completed(request, pk):
    """
    Mark a task as completed. POST /api/tasks/<pk>/complete/
    """
    task = get_object_or_404(Task, pk=pk)
    if task.status == Task.STATUS_COMPLETED:
        return Response({'detail': 'Task already completed.'}, status=status.HTTP_200_OK)
    task.status = Task.STATUS_COMPLETED
    task.save()
    serializer = TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)
