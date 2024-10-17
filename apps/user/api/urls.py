from django.urls import path
from apps.user.api.api import user_api_view

urlpatterns = [
    path('usuario/', user_api_view, name='usuario_api'),
]