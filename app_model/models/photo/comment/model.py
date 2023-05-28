from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Comment(models.Model):
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('MyCustomUser', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    comments = GenericRelation('self')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'Comments'
        ordering = ('created',)

    def __str__(self):
        return f'Comments by {self.author}'

