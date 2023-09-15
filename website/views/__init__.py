# import website.views
# from base import BaseView
from website.views.session.logout import UserLogoutView
from website.views.user.registration import UserRegistrationView #registration_view
from website.views.session.login import UserLoginView
from website.views.photos.upload_photo import UploadPhotoView
from website.views.user.edit_user_profile import EditUserProfileView #edit_user_profile_view

from website.views.photos.likes import LikeView
from website.views.photos.comments import CommentView
from website.views.photos.search import SearchPhotoView
