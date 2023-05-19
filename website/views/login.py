from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View

from website.forms import AuthenticationUserForm

class UserLoginView(View):
    template_name = 'website/user/login.html'
    context = {}

    def get(self, request):
        form = AuthenticationUserForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = AuthenticationUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("base")
            else:
                context = {'form': form,
                           'error_auth': 'Enter correct data!'}
                return render(request, self.template_name, context)
        else:
            context = {'form': form}
            return render(request, self.template_name, context)

# def login_view(request):
#     template_name = 'website/login.html'
#     context = {}
#     if request.POST:
#         form = AuthenticationUserForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(email=email, password=password)
#             if user:
#                 login(request, user)
#                 return redirect("base")
#             else:
#                 context = {'form': form,
#                            'error_auth': 'Enter correct data!'}
#                 return render(request, template_name, context)
#         else:
#             context = {'form': form}
#             return render(request, template_name, context)
#     else:
#         form = AuthenticationUserForm()
#         context = {'form': form}
#         return render(request, template_name, context)