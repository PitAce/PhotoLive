# import website.views
# from base import BaseView
from website.views.main import BaseView
from website.views.session.logout import UserLogoutView
from website.views.user.registration import UserRegistrationView #registration_view
from website.views.session.login import UserLoginView
from website.views.photo.upload_photo import UploadPhotoView
from website.views.user.edit_user_profile import EditUserProfileView #edit_user_profile_view
from website.views.photo.show_details_photo import ShowDetailsPhotoView
from website.views.photo.likes import LikeView
from website.views.photo.comments import CommentView
