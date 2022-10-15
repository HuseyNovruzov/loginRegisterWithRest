from rest_framework import generics, permissions
from accounts.models import NewUser
from .serializers import UserRegisterSerializer, UserLogin
from rest_framework.views import APIView
# from rest_framework_simplejwt.authentication import 
# Create your views here.

class CreateUser(generics.CreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserRegisterSerializer


