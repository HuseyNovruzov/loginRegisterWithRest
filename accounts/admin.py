from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib import admin
from .models import NewUser

class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('email', 'user_name', 'is_staff', 'is_superuser', 'is_active',)
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('user_name',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff',)})
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'user_name', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(NewUser, UserAdmin)
