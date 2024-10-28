from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.user.models import User
from apps.user.api.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all().values('id', 'username', 'email', 'password')
        users_serializer = UserSerializer(users, many=True)

        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        users_serializer = UserSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({'mensaje': 'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail_api_view(request, pk=None):
    #consulta o queryset
    user = User.objects.filter(id=pk).first()
    #validacion
    if user:
        #obtener un usuario
        if request.method == 'GET':
            
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        #actualizar un usuario
        elif request.method == 'PUT':
            user = User.objects.filter(id=pk).first()
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #eliminar un usuario
        elif request.method == 'DELETE':
            user = User.objects.filter(id=pk).first()
            user.delete()
            return Response({'message': 'Usuario eliminado correctamente'}, status=status.HTTP_200_OK)
    return Response({'message': 'No se ha encontrado un usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)