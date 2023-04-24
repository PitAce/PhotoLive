# import website.views
# from base import BaseView
from website.views.main import BaseView
from website.views.logout import UserLogoutView
from website.views.registration import UserRegistrationView #registration_view
from website.views.login import UserLoginView
from website.views.user_profile import UserProfileView #user_profile
from website.views.edit_user_profile import EditUserProfileView #edit_user_profile_view
from website.views.show_details_photo import ShowDetailsPhotoView
from website.views.likes import LikeView