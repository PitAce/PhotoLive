from django.shortcuts import render, redirect
from django.views import View
from app_model.models import Comment, Photo
from website.forms import CommentForm

class CommentView(View):
    ACCEPTABLE_TYPES = {"photo": Photo,
                        "comment": Comment}

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            content_object = self.ACCEPTABLE_TYPES[kwargs['content_type']].objects.get(id=kwargs['content_id'])
            photo_id = kwargs["content_id"] if kwargs["content_type"] == "photo" else content_object.photo_id
            Comment.objects.create(content_object=content_object,
                                   photo_id=photo_id,
                                   text=form.cleaned_data['text'],
                                   author_id=request.user.id,)
        return redirect('retrieve_update_delete_photo', pk=photo_id)

