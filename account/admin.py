from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'birth_date', 'organization', 'user_verified')
    list_filter = ('user_verified', 'moder_verified',
                   'reviewer_verified', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'organization')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'birth_date',
         'organization', 'scientific_degree', 'another_information', 'image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_verified',
         'moder_verified', 'reviewer_verified', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
