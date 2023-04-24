from django import forms

from app_model.models.photo.model import Photo


class UploadPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'image', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }