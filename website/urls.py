from django.urls import path, include
from django.views.generic import TemplateView

from .views import (UserLogoutView, BaseView, registration_view, ShowDetailsPhoto,
                    login_view, edit_user_profile_view,
                    user_profile)

urlpatterns = [
    path('', BaseView.as_view()),
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', user_profile, name='profile'),
    path('photo/<int:pk>/', ShowDetailsPhoto.as_view(), name='details_photo'),
    path('edit_profile/', edit_user_profile_view, name='edit_profile'),

    path('social-auth/', include('social_django.urls', namespace='social')),
]