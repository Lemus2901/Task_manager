# tasks/api/urls.py
from django.urls import path
from apps.tasks.api.Task_view import TaskListCreateView, TaskDetail  # Asegúrate de importar correctamente

urlpatterns = [
    path('tareas/', TaskListCreateView.as_view(), name='task_list_create'),
    path('tarea/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
]
