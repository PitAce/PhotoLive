from django.shortcuts import render
from django.views import View
from website.forms import UploadPhotoForm

class UploadPhotoView(View):
    template_name = 'website/user/profile.html'
    def get(self, request):
        form = UploadPhotoForm()
        return render(request, self.template_name, {'form': form})

