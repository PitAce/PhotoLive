# from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.views import View
from app_model.models import Comment, Photo
from website.forms import CommentForm

class CommentView(View):

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        # import pdb
        # pdb.set_trace()
        if kwargs['content_object_key'] == 'photo':
            content_object = Photo.objects.get(id=kwargs['photo_id'])
        else:
            content_object = Comment.objects.get(id=kwargs['comment_id'])

        if form.is_valid():
            Comment.objects.create(content_object=content_object,
                                        photo_id=kwargs["photo_id"],
                                        text=form.cleaned_data['text'],
                                        author_id=request.user.id,)
        return redirect('details_photo', pk=kwargs['photo_id'])
