# Generated by Django 4.1.7 on 2023-05-02 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_model', '0009_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycustomuser',
            name='liked_photos',
            field=models.ManyToManyField(related_name='liked_users', related_query_name='liked_users', through='app_model.Like', to='app_model.photo'),
        ),
        migrations.AlterField(
            model_name='like',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_model.photo'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
