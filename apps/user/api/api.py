from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.user.models import User
from apps.user.api.serializers import UserSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all().values('id', 'username', 'email', 'password')
        users_serializer = UserSerializer(users, many=True)

        return Response(users_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        users_serializer = UserSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({'mensaje':'usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)