from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView

from .views import (UserLogoutView, BaseView, UserLoginView,
                    UserRegistrationView, ShowDetailsPhoto,  # registration_view,
                    EditUserProfileView, UserProfileView,
                    )  # user_profile)


urlpatterns = [
    path('', BaseView.as_view()),
    # path('register/', registration_view, name='register'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', login_required(UserProfileView.as_view()), name='profile'),
    path('photo/<int:pk>/', ShowDetailsPhoto.as_view(), name='details_photo'),
    path('edit_profile/', login_required(EditUserProfileView.as_view()), name='edit_profile'),

    path('social-auth/', include('social_django.urls', namespace='social')),
]