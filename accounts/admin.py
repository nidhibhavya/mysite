# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Define the fields to be used in the user model in the admin interface
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'gender')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    # These fields are displayed in the form to add or edit a user
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'gender', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'gender', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )

# Register the custom user model with the admin interface
admin.site.register(CustomUser, CustomUserAdmin)
