from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserAdminConfig(UserAdmin):

    search_fields = ('email', 'user_name', 'first_name')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
