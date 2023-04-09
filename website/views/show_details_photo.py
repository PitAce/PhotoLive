from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from app_model.models import Photo


class ShowDetailsPhoto(ListView):
    model = Photo
    template_name = 'website/details_photo.html'
    context_object_name = 'photo'

    def get_queryset(self):
        return Photo.objects.get(id=self.kwargs['pk'])

# class ShowDetailsPhoto(TemplateView):
#     template_name = 'website/details_photo.html'

#     def get(self, request, *args, **kwargs):
#         photo = Photo.objects.get(id=kwargs['pk'])
#         return render(request, self.template_name, {'photo': photo})
