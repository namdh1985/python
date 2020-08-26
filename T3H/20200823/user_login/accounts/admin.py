from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'phone', 'email', 'address']
    fieldsets = (*UserAdmin.fieldsets,
                    ('Thông tin khác', {
                        'fields': ['phone', 'address']
                    })
                )

admin.site.register(CustomUser, CustomUserAdmin)