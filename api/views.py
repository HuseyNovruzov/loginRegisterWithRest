from django.shortcuts import redirect, get_object_or_404
from rest_framework import generics, permissions
from accounts.models import NewUser
from .serializers import (
    UserRegisterSerializer, 
    VerifyEmailSerializer,
    SendLinkSerializer)
from rest_framework import status
from rest_framework.response import Response
import pyotp
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime
from django.utils.timezone import utc


class CreateUser(generics.CreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserRegisterSerializer

    
class SendLinkView(generics.CreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = SendLinkSerializer

    def post(self, request):
        serializer = SendLinkSerializer(data=request.data)
        
        user = get_object_or_404(NewUser,email=request.data.get('email'))
        totp = pyotp.TOTP('base32secret3232', interval=2*60, digits=6)
        otp = totp.now()
        if serializer.is_valid():
            message = render_to_string('activate.html',{
                'user': user,
                'otp': otp
            })
            user.otp=otp
            user.save()
            email = EmailMessage('Email activation',message, to=[request.data.get('email')])
            email.send()
            return Response({'otp': otp, 'email': user.email})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VerifyEmailView(generics.CreateAPIView):

    serializer_class = VerifyEmailSerializer
    def post(self, request):
        user = get_object_or_404(NewUser,email=request.data.get('email'))
        timediff = datetime.utcnow().replace(tzinfo=utc) - user.otp_live_time

        if timediff.total_seconds() < 120 and user.otp == request.data.get('otp'):
            user.is_active = True
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(generics.CreateAPIView):
    pass