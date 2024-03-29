import os.path
import shutil

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View

from app_model.models import MyCustomUser, UserProfile
from website.forms import UpdateUserForm, UpdateUserAvatarForm

class EditUserProfileView(View):
    template_name = 'website/user/edit_profile.html'

    def get(self, request):
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserAvatarForm(instance=request.user.userprofile)
        # import pdb
        # pdb.set_trace()
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateUserAvatarForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user = MyCustomUser.objects.get(id=request.user.id)
            if user.userprofile.avatar and request.FILES:
                    # for delete old thumbnail avatar that was maked imagekit
                path_old_avatar_imgkit = os.path.splitext(user.userprofile.avatar.name)[0]
                shutil.rmtree('media/' + path_old_avatar_imgkit, ignore_errors=True)  # delete dir with all old thumbnail avatar
                from imagekit.utils import get_cache
                get_cache().clear()

                if user.userprofile.avatar != 'default.jpg':
                    user.userprofile.avatar.delete()
                # This for save image with called username from 'form'
                # user.userprofile.avatar.save(f"{request.POST['username']}.{img_format}", request.FILES['avatar'].file)
            user_form.save()
            # profile_form.save()
            return redirect(to='base')
        else:
            self.get(request)

# @login_required
# def edit_user_profile_view(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateUserAvatarForm(request.POST, request.FILES, instance=request.user.userprofile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = MyCustomUser.objects.get(id=request.user.id)
#             if user.userprofile.avatar and request.FILES:
#                     # for delete old thumbnail avatar that was maked imagekit
#                 path_old_avatar_imgkit = os.path.splitext(user.userprofile.avatar.name)[0]
#                 shutil.rmtree('media/' + path_old_avatar_imgkit, ignore_errors=True)  # delete dir with all old thumbnail avatar
#                 from imagekit.utils import get_cache
#                 get_cache().clear()
#
#                 if user.userprofile.avatar != 'default.jpg':
#                     user.userprofile.avatar.delete()
#                 # This for save image with called username from 'form'
#                 # user.userprofile.avatar.save(f"{request.POST['username']}.{img_format}", request.FILES['avatar'].file)
#             user_form.save()
#             # profile_form.save()
#             return redirect(to='base')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateUserAvatarForm(instance=request.user.userprofile)
#     return render(request, 'website/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})