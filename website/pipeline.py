from PIL import Image
import requests
from io import BytesIO
from urllib.parse import urlparse

def get_avatar_img(backend, user, response, *args, **kwargs):

    if backend.name == 'github' and (user.userprofile.avatar == 'default.jpg' or not user.userprofile.avatar):

        avatar_url = urlparse(response['avatar_url'])
        filename = avatar_url.path.split('/')[-1]

        avatar_response = requests.get(response['avatar_url'])
        img_io = BytesIO(avatar_response.content)
        img = Image.open(img_io)
        user.userprofile.avatar.save(f"{filename}.{img.format.lower()}", img_io)

