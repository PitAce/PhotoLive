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

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Need add a vailed email address")

    class Meta:
        model = MyCustomUser
        fields = ("email", "username", "password1", "password2")
