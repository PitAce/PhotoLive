from django import forms
from app_model.models import MyCustomUser


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(required=True,
                               label="Username:",
                               widget=forms.TextInput(attrs={'class': 'form-control'}),)
    email = forms.EmailField(max_length=60,
                             required=True,
                             label="Email:",
                             widget=forms.EmailInput(attrs={"class": "form-control"}),)

    class Meta:
        model = MyCustomUser
        fields = ['username', 'email']