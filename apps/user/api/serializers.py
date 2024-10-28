from rest_framework import serializers
from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'required': True,  # Aseguramos que sea obligatorio
                'error_messages': {'unique': 'Este correo ya está registrado.'}
            },
            'username': {
                'required': True,  # Aseguramos que sea obligatorio
                'error_messages': {'unique': 'Este nombre de usuario ya está en uso.'}
            }
        }


    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return value

    def validate_username(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El nombre de usuario debe tener al menos 5 caracteres.")
        return value

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Introduce una dirección de correo electrónico válida.")
        return value



    def create(self, validated_data):
        # Extraer el campo groups si existe
        groups = validated_data.pop('groups', None)
        
        # Crear el usuario sin asignar directamente el campo groups
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        
        # Asignar grupos si hay
        if groups:
            user.groups.set(groups)
        
        return user


    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        password = validated_data.get('password', None)
        if password:
            update_user.set_password(password)
            update_user.save()
        return update_user


class UserListSerializer(serializers.Serializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
        }
