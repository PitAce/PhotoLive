from django import forms
from app_model.models.photo.comment.model import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        # widgets = {
        #     'text': forms.TextInput(attrs={'class': 'form-control'}),
        # }