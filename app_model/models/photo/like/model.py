from django.db import models

class Like(models.Model):
    user = models.ForeignKey('MyCustomUser', on_delete=models.CASCADE, related_name='likes', related_query_name='likes')
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='likes', related_query_name='likes')

    class Meta:
        db_table = 'likes'
