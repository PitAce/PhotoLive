from django.shortcuts import render, redirect
from django.views import View
from app_model.models import Photo

class BaseView(View):
    template_name = 'website/base.html'
    def get(self, request, *args, **kwargs):
        user_photo = Photo.objects.all()
        return render(request, self.template_name, {'user_photo': user_photo})