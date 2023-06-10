from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from app_model.models.user.manager import UserManager



class MyCustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=150)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    liked_photos = models.ManyToManyField('Photo', related_name='liked_users', related_query_name="liked_users", through='like')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.email

