from django import forms
from app_model.models import MyCustomUser


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
