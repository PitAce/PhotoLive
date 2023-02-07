from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from photo_live.users.forms import CustomUserCreationForm, CustomUserChangeForm
from photo_live.models_app.models import MyCustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = MyCustomUser
    list_display = ("username", "email", "is_staff", "is_active",)
    list_filter = ("username", "email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
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
