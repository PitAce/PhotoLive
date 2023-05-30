from django import forms
from app_model.models.photo.comment.model import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'style': 'background:#fff', 'placeholder': 'New comment...'}), label='')
    class Meta:
        model = Comment
        fields = ['text']
