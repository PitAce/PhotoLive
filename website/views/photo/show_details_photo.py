from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView
from app_model.models.photo.model import Photo
from app_model.models.photo.comment.model import Comment
from website.forms import CommentForm
from website.views.photo.comments import CommentView


class ShowDetailsPhotoView(View):
    template_name = 'website/main/photos/show_details_photo.html'

    def get(self, request, *args, **kwargs):
        photo = Photo.objects.get(id=kwargs['pk'])
        comments = Comment.objects.filter(object_id=kwargs['pk'])
        form = CommentForm()
        return render(request, self.template_name, {'photo': photo, 'comments': comments, 'form': form})

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


# class ShowDetailsPhoto(DetailView):
#     model = Photo
#     template_name = 'website/details_photo.html'
#     context_object_name = 'photo'
#     pk_url_kwarg = 'pk'