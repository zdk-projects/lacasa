from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from realestate.models import Album, AlbumImage
from realestate.views import about_us


def gallery(request):
    list = Album.objects.filter(is_visible=True).order_by('-created')
    paginator = Paginator(list, 10)

    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        albums = paginator.page(
            paginator.num_pages)  # If page is out of range (e.g.  9999), deliver last page of results.
    content = {
        'about_us': about_us(),
        'header': {
            'title': 'Image Gallery',
        },
        'nbar': 'gallery',
    }
    return render(request, 'pages/image-gallery/gallery.html', {'albums': albums, 'content': content})


def album_details(request, slug):
    context = model_to_dict(get_object_or_404(Album, slug=slug))
    context["images"] = AlbumImage.objects.filter(album=context["id"])
    content = {
        'about_us': about_us(),
        'nbar': 'gallery',
        'album': context,
        'header': {
            'title': [
                {
                    'title': 'Image Gallery',
                    'url': 'gallery',
                },
                context["title"]
            ],
        }
    }

    return render(request, 'pages/image-gallery/album_detail.html', {'content': content})


class AlbumDetail(DetailView):
    model = Album

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the images
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        return context


def handler404(request, exception):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)
