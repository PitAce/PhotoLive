from django.contrib.auth.decorators import login_required
from django.urls import path, include

from .views import (UserLogoutView, UserLoginView,
                    UserRegistrationView,
                    EditUserProfileView, UploadPhotoView, LikeView, CommentView
                    )
from .views.photo import PhotoListCreateView, RetrieveUpdateDeletePhotoView

urlpatterns = [
    # user
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('upload_photo/', login_required(UploadPhotoView.as_view()), name='upload_photo'),
    path('edit_profile/', login_required(EditUserProfileView.as_view()), name='edit_profile'),
    # photo
    path('photos/', PhotoListCreateView.as_view(), name='photo_list_create'),
    path('photo/<int:pk>/', RetrieveUpdateDeletePhotoView.as_view(), name='retrieve_update_delete_photo'),
    # photo details
    path('<str:content_type>/<int:content_id>/comments', CommentView.as_view(), name='add_comment'),
    path('photo/<int:photo_pk>/likes', LikeView.as_view(), name='like'),
    # social-auth
    path('social-auth/', include('social_django.urls', namespace='social')),
]