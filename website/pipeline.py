from urllib.request import urlopen
from django.core.files.base import ContentFile

def get_avatar_img(backend, user, response, *args, **kwargs):
    if backend.name == 'github':
        avatar_img = urlopen(response['avatar_url'])

        # save picture if user haven't avatar
        if not user.userprofile.avatar:
            user.userprofile.avatar.save(
                "{0}.jpg".format(user.username),
                ContentFile(avatar_img.read()),
            )

