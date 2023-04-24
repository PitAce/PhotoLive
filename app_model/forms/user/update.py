from django import forms
from django.contrib.auth.forms import UserChangeForm
from app_model.models import MyCustomUser


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = MyCustomUser
        fields = ("email",)

