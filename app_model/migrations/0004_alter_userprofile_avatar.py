# Generated by Django 4.1.7 on 2023-03-24 14:44

from django.db import migrations, models
import utils.file_uploader


class Migration(migrations.Migration):

    dependencies = [
        ('app_model', '0003_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=utils.file_uploader.uploaded_file_path),
        ),
    ]
