# Generated by Django 4.1.7 on 2023-04-08 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_model', '0006_alter_userimages_description_alter_userimages_image_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserImages',
            new_name='UserPhoto',
        ),
    ]
