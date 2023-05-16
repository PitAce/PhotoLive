from django.db import models
# from app_model.models import MyCustomUser, Photo

class Like(models.Model):
    user = models.ForeignKey('MyCustomUser', on_delete=models.CASCADE, related_name='likes')
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='likes')
    # liked = models.BooleanField(default=False)

    class Meta:
        db_table = 'Like'
