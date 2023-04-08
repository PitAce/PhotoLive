from django.db import models
from app_model.models.my_custom_user import MyCustomUser

from django.core.validators import FileExtensionValidator


class UserPhoto(models.Model):
    user = models.ForeignKey(MyCustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='images/', blank=False, validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg'])])
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.title