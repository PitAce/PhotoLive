# from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.views import View
from app_model.models import Comment, Photo
from website.forms import CommentForm

class CommentView(View):

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(content_object=Photo.objects.get(id=kwargs['id']),
                                        photo_id=kwargs["id"],
                                        text=form.cleaned_data['text'],
                                        author_id=request.user.id,)
        return redirect('details_photo', pk=kwargs['id'])
