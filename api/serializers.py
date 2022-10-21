from rest_framework import serializers
from accounts.models import NewUser
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
        UniqueValidator(
            queryset=NewUser.objects.all(),
            message="Email already exists"
        )
    ])
    user_name = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = NewUser
        fields = ('email', 'user_name','password',)
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = NewUser.objects.create_user(**validated_data)
        return user


class SendLinkSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    

class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(max_length=6, required=True)

class ResetPasswordSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6, required=6)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True)

    
    