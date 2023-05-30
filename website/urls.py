from django.contrib.auth.decorators import login_required
from django.urls import path, include

from .views import (UserLogoutView, BaseView, UserLoginView,
                    UserRegistrationView, ShowDetailsPhotoView,
                    EditUserProfileView, UploadPhotoView, LikeView, CommentView
                    )


urlpatterns = [
    path('', BaseView.as_view()),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', login_required(UploadPhotoView.as_view()), name='profile'),

    path('photo/<int:pk>/', ShowDetailsPhotoView.as_view(), name='details_photo'),
    path('photo/<int:photo_id>/<int:comment_id>/<slug:content_object_key>/', CommentView.as_view(), name='add_comment'),
    path('edit_profile/', login_required(EditUserProfileView.as_view()), name='edit_profile'),
    path('like/<int:photo_pk>/', LikeView.as_view(), name='like'),



    path('social-auth/', include('social_django.urls', namespace='social')),
]