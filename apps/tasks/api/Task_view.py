# tasks/api/api.py
from rest_framework import generics
from apps.tasks.models import Task
from apps.tasks.api.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtra las tareas solo para el usuario autenticado
        return self.queryset.filter(user=self.request.user)
    
    
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer