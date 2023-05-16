from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from django.core.paginator import Paginator
from app_model.models.photo.model import Photo


# class BaseView(ListView):
#     model = Photo
#     template_name = 'website/base.html'
#     context_object_name = 'user_photo'
#
#     def get_queryset(self):
#         return Photo.objects.all()

class BaseView(View):
    template_name = 'website/base.html'
    def get(self, request, *args, **kwargs):
        all_users_photos = Photo.objects.all()
        paginator = Paginator(all_users_photos, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # if page_number:
        #     import pdb
        #     pdb.set_trace()
        return render(request, self.template_name, {'page_obj': page_obj})
