from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (('Personnal Info'), {'fields': ('full_name', 'phone', 'gender', 'birthday', 'profile')}),
        (('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        (('Importants dates'), {'fields': ('last_login', 'date_joined')}),
    )

    """For new User"""
    add_fieldsets =(
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    ) 
    list_display = ('username','email', 'full_name', 'is_staff')
    search_fields = ('username', 'email', 'full_name')
    ordering = ('username',)


admin.site.register(get_user_model(), CustomUserAdmin)
