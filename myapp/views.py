from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader


def index(request):
    all_albums=Album.objects.all()
    context={'all_albums':all_albums}
    return render(request,'myapp/index.html',context)

def detail(request,album_id):
    try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album doesn't exist")
    return render(request,'myapp/detail.html',{'album':album})
