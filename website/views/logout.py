from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.views import View


class UserLogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('base')
