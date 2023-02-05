from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm


def registration_view(request):

    template_name = 'users/register.html'
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect("base.html")
        else:
            context = {'form': form}
            return render(request, template_name, context)
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, template_name, context)





