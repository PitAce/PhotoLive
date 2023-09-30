from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator

from app_model.models import UserProfile, Comment
from app_model.models.photo.model import Photo

from website.forms import UploadPhotoForm, CommentForm
from django.db.models import Count
from website.services.sort_photo_by_user_choise import sort_photo


class PhotoListCreateView(View):
    template_name = 'website/base.html'
    def get(self, request, *args, **kwargs):
        context = {}
        context['text_for_sort_buttom'] = 'по умолчанию'  # this is a temporary solution

        if 'sort_by' in kwargs:
            all_users_photos = sort_photo(kwargs['sort_by'])
            context['text_for_sort_buttom'] = kwargs['sort_by']  # this is a temporary solution
        else:
            all_users_photos = Photo.objects.all()

        paginator = Paginator(all_users_photos, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UploadPhotoForm(request.POST, request.FILES)

        if form.is_valid():
            user_img = form.save(commit=False)
            user_img.user = request.user
            user_img.save()
            return redirect(to='base')
        return render(request, 'website/user/profile.html', {'form': form})



class RetrieveUpdateDeletePhotoView(View):
    template_name = 'website/main/photos/show_details_photo.html'

    def get(self, request, *args, **kwargs):
        photo = Photo.objects.get(id=kwargs['pk'])
        comments = Comment.objects.filter(object_id=kwargs['pk'])
        form = CommentForm()
        return render(request, self.template_name, {'photo': photo, 'comments': comments, 'form': form})

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass