from django import forms
from django.contrib.auth.forms import UserCreationForm
from app_model.models import MyCustomUser


class UserCreateForm(UserCreationForm):

    class Meta:
        model = MyCustomUser
        fields = ("email",)

