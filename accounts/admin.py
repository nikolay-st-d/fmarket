from django.contrib import admin
from django.contrib.auth import get_user_model

from accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_filter = ['is_staff', 'is_active']
    readonly_fields = ['date_joined']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ['country']
    list_display = ['first_name', 'last_name', 'country']
