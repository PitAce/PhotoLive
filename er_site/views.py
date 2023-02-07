from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AuthenticationUserForm


def registration_view(request):
    template_name = 'site/register.html'
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect("base")
        else:
            context = {'form': form}
            return render(request, template_name, context)
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect("base")


def login_view(request):
    template_name = 'site/login.html'
    context = {}
    if request.POST:
        form = AuthenticationUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("base")
        else:
            context = {'form': form}
            return render(request, template_name, context)
    else:
        form = AuthenticationUserForm()
        context = {'form': form}
        return render(request, template_name, context)





