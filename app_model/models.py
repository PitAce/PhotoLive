from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from .managers import CustomUserManager

class MyCustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=150)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(MyCustomUser, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='images/avatar/')

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=MyCustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.userprofile.save()
    except ObjectDoesNotExist:
        UserProfile.objects.create(user=instance)

