from django.shortcuts import render, redirect
from django.views import View
from app_model.models import Comment, Photo
from website.forms import CommentForm

class CommentView(View):

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        acceptable_types = {"photo": Photo,
                            "comment": Comment}

        content_object = acceptable_types[kwargs['content_type']].objects.get(id=kwargs['content_id'])
        if form.is_valid():
            Comment.objects.create(content_object=content_object,
                                        photo_id=kwargs["photo_id"],
                                        text=form.cleaned_data['text'],
                                        author_id=request.user.id,)
        return redirect('details_photo', pk=kwargs['photo_id'])

