from django import forms
from django.contrib.auth.forms import UserCreationForm
from photo_live.models_app.models import MyCustomUser




class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        help_text="Enter your name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name'})
    )
    email = forms.EmailField(
        max_length=60,
        help_text="Enter a vailed email address",
        widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Email'}),
    )
    password1 = forms.CharField(
        help_text="Enter a password",
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Password1'}),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Password2'}),
        help_text="Enter the same password as before"
    )

    class Meta:
        model = MyCustomUser
        fields = ("username", "email", "password1", "password2",)


class AuthenticationUserForm(forms.Form):
    email = forms.EmailField(
        max_length=60,
        help_text="Enter a your email",
        widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Email'}),
    )
    password = forms.CharField(
        help_text="Enter your password",
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Password'}),
    )

    class Meta:
        model = MyCustomUser
        fields = ("email", "password",)



