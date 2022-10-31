from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class CustomBaseUserManager(BaseUserManager):

    def create_user(self, email, user_name, password, **other_fields):
        
        if not email:
            raise ValueError(
                _("Email must be provided")
            )
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if not other_fields.get("is_staff"):
            raise ValueError(
                _("Superuser must be assigned is_staff=True")
            )
        if not other_fields.get("is_superuser"):
            raise ValueError(
                _("Superuser must be assigned is_superuser=True")
            )
        return self.create_user(email, user_name, password, **other_fields)

class NewUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_("Email address"), unique=True)
    user_name = models.CharField(_("Username"), max_length=150)
    otp = models.CharField(default='0',max_length=6)
    otp_live_time = models.DateTimeField(auto_now=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomBaseUserManager()

    REQUIRED_FIELDS = ['user_name']
    USERNAME_FIELD = 'email'
        
