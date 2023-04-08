from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app_model.models import UserProfile
from website.forms import UserPhotoForm


@login_required
def user_profile(request):
    user_avatar = UserProfile.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form = UserPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            user_img = form.save(commit=False)
            user_img.user = request.user
            user_img.save()
            return redirect(to='base')
    else:
        form = UserPhotoForm()
    return render(request, 'website/profile.html', {'user_avatar': user_avatar, 'form': form})