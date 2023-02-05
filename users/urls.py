from django.urls import path, include

from .views import registration_view

urlpatterns = [
    path('', include('users.urls')),
    path('register/', registration_view, name="register"),
]
