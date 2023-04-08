from django import forms
from app_model.models import UserProfile


class UpdateUserAvatarForm(forms.ModelForm):
    avatar = forms.ImageField(label="Avatar:",
                              widget=forms.FileInput(attrs={'class': 'form-control-file'}),)

    class Meta:
        model = UserProfile
        fields = ['avatar']