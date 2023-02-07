from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyCustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = MyCustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = MyCustomUser
        fields = ("email",)





