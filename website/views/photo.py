from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator

from app_model.models import UserProfile, Comment
from app_model.models.photo.model import Photo

from website.forms import UploadPhotoForm, CommentForm
from django.db.models import Count

class PhotoListCreateView(View):
    template_name = 'website/base.html'
    def get(self, request, *args, **kwargs):
        # sort_photo
        all_users_photos = Photo.objects.all()
        # if 'choice_sort_photos_by' in request.GET:
        #     request.session['sort_by'] = request.GET.get('choice_sort_photos_by')
        #     request.session.modified = True
        # #  QUERY!!!
        # if 'sort_by' in request.session:
        #     if request.session['sort_by'] == 'created_at':
        #         all_users_photos = Photo.objects.all().order_by("-" + request.session['sort_by'])
        #     else:
        #         all_users_photos = Photo.objects.all().annotate(sort_photo_list=Count(request.session.get('sort_by'))).order_by('-sort_photo_list')
        #
        # form = UploadPhotoForm()
        paginator = Paginator(all_users_photos, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # import pdb
        # pdb.set_trace()
        return render(request, self.template_name, {'page_obj': page_obj, "form": 0})#form})

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