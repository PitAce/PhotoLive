# Generated by Django 4.1.7 on 2023-06-10 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.file_uploader


class Migration(migrations.Migration):

    dependencies = [
        ('app_model', '0013_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created_at',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='created',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=utils.file_uploader.uploaded_file_path),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
        migrations.AlterModelTable(
            name='like',
            table='like',
        ),
        migrations.AlterModelTable(
            name='photo',
            table='photo',
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='user_profile',
        ),
    ]