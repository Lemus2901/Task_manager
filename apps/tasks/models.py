from django.db import models
from apps.user.models import User

class Task(models.Model):  # Cambiado a mayúscula
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=100)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "Completed" if self.complete else "Pending"
        return f"{self.title} ({status})"

    class Meta:
        ordering = ['complete', '-created']  # Primero completas, luego recientes
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
