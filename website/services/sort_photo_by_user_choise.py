from django.db.models import Count
from app_model.models.photo.model import Photo


def sort_photo(sort_choice):
        if sort_choice == 'created_at':
            return Photo.objects.all().order_by("-" + sort_choice)
        else:
            return Photo.objects.all().annotate(sort_photo_list=Count(sort_choice)).order_by('-sort_photo_list')


    # request.session['sort_choice'] = sort_choice
    # request.session.modified = True
    #  QUERY!!!
    # if 'sort_choice' in request.session:
    #     if request.session['sort_choice'] == 'created_at':
    #         return Photo.objects.all().order_by("-" + request.session['sort_choice'])
    #     else:
    #         return Photo.objects.all().annotate(sort_photo_list=Count(request.session.get('sort_choice'))).order_by('-sort_photo_list')

