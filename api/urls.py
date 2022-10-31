from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)
from .views import CreateUser, VerifyEmailView, SendLinkView, ResetPasswordView

app_name = 'api'

urlpatterns = [
    path('register/', CreateUser.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('send-otp/', SendLinkView.as_view(), name='link'),
    path('verify-otp/', VerifyEmailView.as_view(), name='otp'),
    path('reset-password/', ResetPasswordView().as_view(), name='reset-password')
]