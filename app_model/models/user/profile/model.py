from django.db import models

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from app_model.models.user.my_custom_user import MyCustomUser
from utils.file_uploader import uploaded_file_path, skip_saving_file, save_file

from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill

class UserProfile(models.Model): #Profile
    user = models.OneToOneField('MyCustomUser', on_delete=models.CASCADE, related_name='user_profile', related_query_name="user_profile")
    avatar = models.ImageField(blank=True, default='default.jpg', upload_to=uploaded_file_path)

    avatar_small_for_photo_info = ImageSpecField(source='avatar',
                                  processors=[ResizeToFill(20, 20)],
                                  format='JPEG',
                                  options={'quality': 60})
    avatar_small = ImageSpecField(source='avatar',
                                  processors=[ResizeToFill(50, 50)],
                                  format='JPEG',
                                  options={'quality': 60})

    avatar_medium = ImageSpecField(source='avatar',
                                  processors=[ResizeToFit(100, 100)],
                                  format='JPEG',
                                  options={'quality': 90})

    avatar_big = ImageSpecField(source='avatar',
                                  processors=[ResizeToFit(180, 160)],
                                  format='JPEG',
                                  options={'quality': 90})

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'user_profiles' #profiles




@receiver(post_save, sender=MyCustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.user_profile.save()
    except ObjectDoesNotExist:
        UserProfile.objects.create(user=instance)

@receiver(pre_save, sender=UserProfile)
def user_profile_skip_saving_files(sender, instance, **kwargs):
    skip_saving_file(sender, instance, **kwargs)


@receiver(post_save, sender=UserProfile)
def user_profile_save_files(sender, instance, created, **kwargs):
    save_file(sender, instance, created, **kwargs)
