from django.contrib import admin
from app_model.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'photo', 'text')

admin.site.register(Comment, CommentAdmin)