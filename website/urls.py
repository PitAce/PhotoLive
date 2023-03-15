from django.urls import path, include
from django.views.generic import TemplateView

from .views import (
    registration_view,
    logout_view,
    login_view,
)

urlpatterns = [

    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', TemplateView.as_view(template_name='website/profile.html'), name='profile'),
    path('edit_profile/', edit_user_profile_view, name='edit_profile'),
    path('social-auth/', include('social_django.urls', namespace='social')),

]