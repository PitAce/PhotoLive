from django.urls import path, include
from django.views.generic import TemplateView

from .views import (registration_view, logout_view,
                    login_view, edit_user_profile_view,
                    user_profile, base_view, show_details_photo)

urlpatterns = [
    path('', base_view),
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('photo/<int:pk>/', show_details_photo, name='details_photo'),
    #path('profile/', TemplateView.as_view(template_name='website/profile.html'), name='profile'),
    path('edit_profile/', edit_user_profile_view, name='edit_profile'),

    path('social-auth/', include('social_django.urls', namespace='social')),
]