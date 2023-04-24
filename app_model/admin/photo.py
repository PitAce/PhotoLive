from django.contrib import admin
from django.db.models import F

from app_model.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_username')

    @admin.display(description='Author Name', ordering='user')
    def get_username(self, obj):
        return obj.user.username

admin.site.register(Photo, PhotoAdmin)