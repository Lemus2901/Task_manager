from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'complete', 'created')  # Campos que se mostrarán en la lista
    search_fields = ('title',)  # Permitir búsqueda por título
    list_filter = ('complete',)