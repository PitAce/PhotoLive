from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from app_model.models import Photo
from website.forms import UploadPhotoForm
from django.db.models import Q


# SERVICE
class SearchPhotoView(View):
    template_name = 'website/base.html'
    def get(self, request, *args, **kwargs):
        search = self.request.GET.get('query')
        search_photo = Photo.objects.filter(Q(title__regex=(r"\w*"+search+r"\w*")))# | Q(description__icontains=search))

        # import pdb
        # pdb.set_trace()
        form = UploadPhotoForm()
        paginator = Paginator(search_photo, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # import pdb
        # pdb.set_trace()
        return render(request, self.template_name, {'page_obj': page_obj, "form": form})