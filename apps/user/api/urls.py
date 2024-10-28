from django.urls import path
from apps.user.api.api import user_api_view,user_detail_api_view, register_user

urlpatterns = [
    path('usuario/', user_api_view, name='usuario_api'),
    path('usuario/<int:pk>/', user_detail_api_view, name='usuario_detail_api'),
    path('usuario/register/', register_user, name='register_user')
    
]