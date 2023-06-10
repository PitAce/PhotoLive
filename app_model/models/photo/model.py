from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from app_model.models.user.my_custom_user import MyCustomUser

from django.core.validators import FileExtensionValidator


class Photo(models.Model):
    user = models.ForeignKey('MyCustomUser', on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='images/', blank=False, validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg'])])
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=False)
    comments = GenericRelation('Comment')


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'photo'
