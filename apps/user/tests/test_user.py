from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from apps.user.models import User

class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        response = self.client.post(reverse('usuario_api'), {  # Asegúrate de que esto coincide con tu nombre de URL
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_users(self):
        User.objects.create(username='testuser', email='test@example.com', password='password123')
        response = self.client.get(reverse('usuario_api'))  # Asegúrate de que esto coincide con tu nombre de URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_user(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='password123')
        response = self.client.put(reverse('usuario_detail_api', args=[user.id]), {  # Ruta correcta para la actualización
            'username': 'updateduser',
            'email': 'updated@example.com',
            'password': 'newpassword123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='password123')
        response = self.client.delete(reverse('usuario_detail_api', args=[user.id]))  # Ruta correcta para la eliminación
        self.assertEqual(response.status_code, status.HTTP_200_OK)
