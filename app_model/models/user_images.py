from django.db import models
from app_model.models.my_custom_user import MyCustomUser

from django.core.validators import FileExtensionValidator


class UserImages(models.Model):
    user = models.ForeignKey(MyCustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg'])])
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title