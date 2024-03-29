from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app_model.forms import UserCreateForm, UserUpdateForm
from app_model.models import MyCustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserCreateForm
    form = UserUpdateForm
    model = MyCustomUser
    list_display = ("username", "email", "is_staff", "is_active",)
    list_filter = ("username", "email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "email", "password", "date_joined")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email", "username")


admin.site.register(MyCustomUser, CustomUserAdmin)