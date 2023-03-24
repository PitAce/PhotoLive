import os.path
import shutil

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from app_model.models import MyCustomUser, UserProfile
from .forms import RegistrationForm, AuthenticationUserForm, UpdateUserForm, UpdateUserProfileForm


def registration_view(request):
    template_name = 'website/register.html'
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
    template_name = 'website/login.html'
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
                context = {'form': form,
                           'error_auth': 'Enter correct data!'}
                return render(request, template_name, context)
        else:
            context = {'form': form}
            return render(request, template_name, context)
    else:
        form = AuthenticationUserForm()
        context = {'form': form}
        return render(request, template_name, context)


def user_profile(request):
    user_avatar = UserProfile.objects.get(user_id=request.user.id)
    return render(request, 'website/profile.html', {'user_avatar': user_avatar})

@login_required
def edit_user_profile_view(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user = MyCustomUser.objects.get(id=request.user.id)
                # for delete old thumbnail avatar that was maked imagekit
            path_old_avatar_imgkit = os.path.splitext(user.userprofile.avatar.name)[0]
            shutil.rmtree('media/' + path_old_avatar_imgkit, ignore_errors=True)  # delete dir with all old thumbnail avatar
            from imagekit.utils import get_cache
            get_cache().clear()

            if user.userprofile.avatar and request.FILES:
                user.userprofile.avatar.delete()
                # This for save image with called username from 'form'
                # user.userprofile.avatar.save(f"{request.POST['username']}.{img_format}", request.FILES['avatar'].file)
            user_form.save()
            # profile_form.save()
            return redirect(to='base')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserProfileForm(instance=request.user.userprofile)
    return render(request, 'website/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

















