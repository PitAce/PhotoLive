from django.urls import path, include

from .views import (
    registration_view,
    logout_view,
    login_view,
)

urlpatterns = [

    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),

]