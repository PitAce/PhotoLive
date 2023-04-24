from django.db import models
from app_model.models import MyCustomUser, Photo

class Like(models.Model):
    user = models.ForeignKey(MyCustomUser, null=True, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, null=True, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
