from rest_framework import serializers
from .models import CustomUser


from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):

        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid username or password."
            )

        refresh = RefreshToken.for_user(user)

        return {
            'username': user.username,
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    confirm_password=serializers.CharField(write_only=True)

    class Meta:
        model=CustomUser
        fields=[
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'password',
            'confirm_password',
        ]

    def validate(self,data):
        if data['password']!= data['confirm_password']:
            raise serializers.ValidationError(
                {"confirm password":"password do not match"}
            )
        return data 
    def create(self,validated_data):
        validated_data.pop("confirm_password")

        user=CustomUser.objects.create_user(
            **validated_data
        )

        return user
class ChangePasswordSerializer(serializers.Serializer):

        old_password = serializers.CharField(write_only=True)
        new_password = serializers.CharField(write_only=True)
        confirm_password = serializers.CharField(write_only=True)

        def validate(self, data):

            if data['new_password'] != data['confirm_password']:
                 raise serializers.ValidationError(
            "New password and confirm password do not match"
        )

            return data

