
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from django.views.generic import FormView

from website.forms import RegistrationForm


class UserRegistrationView(View):
    template_name = 'website/register.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect("base")
        else:
            return render(request, self.template_name, {'form': form})



# class UserRegistrationView(FormView):
#     template_name = 'website/register.html'
#     form_class = RegistrationForm
#     success_url = '/'
#
#     def form_valid(self, form):
#         form.save()
#         email = form.cleaned_data["email"]
#         password = form.cleaned_data["password1"]
#         user = authenticate(email=email, password=password)
#         login(self.request, user)
#         return super(UserRegistrationView, self).form_valid(form)




# def registration_view(request):
#     template_name = 'website/register.html'
#     context = {}
#
#     if request.POST:
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data["email"]
#             password = form.cleaned_data["password1"]
#             user = authenticate(email=email, password=password)
#             login(request, user)
#             return redirect("base")
#         else:
#             context = {'form': form}
#             return render(request, template_name, context)
#     else:
#         form = RegistrationForm()
#         context = {'form': form}
#         return render(request, template_name, context)