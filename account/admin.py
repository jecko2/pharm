from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import CustomUser, Profile

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'is_active', 'is_staff']
    


@admin.register(Profile)
class ProfileUserAmin(admin.ModelAdmin):
    list_display = ['user','role', 'is_cleared']
    
