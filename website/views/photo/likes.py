from django.shortcuts import redirect
from app_model.models import Like
from django.views import View


class LikeView(View):

    def post(self, request, *args, **kwargs):
        new_like, created = Like.objects.get_or_create(user=request.user, photo_id=kwargs['photo_pk'])
        if not created:
            Like.objects.filter(user=request.user, photo_id=kwargs['photo_pk']).delete()
            return redirect('/')
        else:
            # new_like.liked = True
            new_like.save()
            return redirect('/')
