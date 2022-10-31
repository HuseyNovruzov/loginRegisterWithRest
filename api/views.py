from django.shortcuts import redirect, get_object_or_404
from rest_framework import generics, permissions
from accounts.models import NewUser
from .serializers import (
    ResetPasswordSerializer,
    UserRegisterSerializer, 
    VerifyEmailSerializer,
    SendLinkSerializer)
from rest_framework import status
from rest_framework.response import Response
import pyotp
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime, timedelta
from django.utils.timezone import utc
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ValidationError


class CreateUser(generics.CreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserRegisterSerializer   

    
class generateOTP:
    @staticmethod
    def returnValue():
        secret = pyotp.random_base32()
        totp = pyotp.TOTP(secret, interval=2*60, digits=6)
        OTP = totp.now()
        return {'totp': secret, 'OTP': OTP}


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
            user.otp_live_time = datetime.utcnow().replace(tzinfo=utc)
            user.save()
            email = EmailMessage('Email activation',message, to=[request.data.get('email')])
            email.send()
            return Response({'email': user.email})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VerifyEmailView(generics.CreateAPIView):

    serializer_class = VerifyEmailSerializer
    def post(self, request):
        user = get_object_or_404(NewUser,email=request.data.get('email'))
        timediff = datetime.utcnow().replace(tzinfo=utc) - user.otp_live_time

        if timediff.total_seconds() < 120 and user.otp == request.data.get('otp') and not user.is_active:
            user.is_active = True
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response({'OTP': "Invalid otp"},status=status.HTTP_406_NOT_ACCEPTABLE) 


class ResetPasswordView(generics.CreateAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):

        user = get_object_or_404(NewUser, email=request.data.get('email'))
        timediff = datetime.utcnow().replace(tzinfo=utc) - user.otp_live_time
        print('Seconds : {}'.format(timediff.total_seconds()))

        if timediff.total_seconds() < 120 and user.otp == request.data.get('otp') and user.is_active:
            try:
                validate_password(request.data.get('password'))
            except Exception as e:
                raise ValidationError(str(e))

            if request.data.get('password') != request.data.get('password_confirm'):
                raise ValidationError("Password did't match!")
            user.set_password(request.data.get('password'))
            # Expire OTP
            print('Before', user.otp_live_time)
            user.otp_live_time = user.otp_live_time - timedelta(minutes=2)
            user.save()
            print('After',user.otp_live_time)

            return Response({'success': "Password has been changed"},status=status.HTTP_200_OK)
        return Response({"OTP": "Invalid OTP"},status=status.HTTP_406_NOT_ACCEPTABLE)