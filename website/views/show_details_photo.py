from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from app_model.models.photo.model import Photo


class ShowDetailsPhoto(DetailView):
    model = Photo
    template_name = 'website/details_photo.html'
    context_object_name = 'photo'
    pk_url_kwarg = 'pk'


    # context_object_name = 'post'


# class ShowDetailsPhoto(ListView):
#     model = Photo
#     template_name = 'website/details_photo.html'
#     context_object_name = 'photo'

#     def get_queryset(self):
#         return Photo.objects.get(id=self.kwargs['pk'])



# class ShowDetailsPhoto(TemplateView):
#     template_name = 'website/details_photo.html'
#
#     def get(self, request, *args, **kwargs):
#         photo = Photo.objects.get(id=kwargs['pk'])
#         return render(request, self.template_name, {'photo': photo})
