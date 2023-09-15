from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from django.core.validators import FileExtensionValidator
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from utils.file_uploader import uploaded_file_path


class Photo(models.Model):
    user = models.ForeignKey('MyCustomUser', on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to=uploaded_file_path, blank=False, validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg'])])
    created_at = models.DateTimeField(auto_now_add=True)
    #update_at for  check cash, take proxy model
    description = models.TextField(blank=False)
    comments = GenericRelation('Comment')
    image_small = ImageSpecField(source='image',    # image_300x300
                                  processors=[ResizeToFill(300, 300)],
                                  format='JPEG',
                                  options={'quality': 60})


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'photos'
