from django.contrib import admin
from app_model.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username',)

    @admin.display(description='User', ordering='user')
    def get_username(self, obj):
        return obj.user.username
admin.site.register(UserProfile, UserProfileAdmin)
