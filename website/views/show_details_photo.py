from django.shortcuts import render
from app_model.models import Photo

def show_details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    return render(request, 'website/details_photo.html', {'photo': photo})