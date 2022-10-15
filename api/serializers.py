from rest_framework import serializers
from accounts.models import NewUser
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
        UniqueValidator(
            queryset=NewUser.objects.all(),
            message="Email already exists"
        )
    ])
    user_name = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(min_length=8, write_only=True, validators=[validate_password])

    class Meta:
        model = NewUser
        fields = ('email', 'user_name','password',)
        extra_kwargs = {'password': {'write_only': True}}

    # def validate(self, data):
    #     try:
    #         user = NewUser(**data)
    #     except ValidationError as e:
    #         raise serializers.ValidationError(e)
    #     try:
    #         validate_password(data['password'], user=user)
    #     except ValidationError as e:
    #         raise serializers.ValidationError(e)
        
    #     return data

    def create(self, validated_data):
        return NewUser.objects.create_user(**validated_data)


class UserLogin(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)    
    
    class Meta:
        model = NewUser
        fields = ('email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    