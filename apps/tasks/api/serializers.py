# tasks/api/serializers.py
from rest_framework import serializers
from apps.tasks.models import Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'complete', 'created']
        read_only_fields = ['id', 'user', 'created']
