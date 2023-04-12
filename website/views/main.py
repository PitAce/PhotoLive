from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from app_model.models.photo.model import Photo


class BaseView(ListView):
    model = Photo
    template_name = 'website/base.html'
    context_object_name = 'user_photo'

    def get_queryset(self):
        return Photo.objects.all()

# class BaseView(View):
#     template_name = 'website/base.html'
#     def get(self, request, *args, **kwargs):
#         user_photo = Photo.objects.all()
#         return render(request, self.template_name, {'user_photo': user_photo})
