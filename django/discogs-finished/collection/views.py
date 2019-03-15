from django.shortcuts import render
from django.http import HttpResponse

from .models import Release

# Create your views here.

def index(request):
    
    releases = Release.objects.all()[:20]
    
    context = {
        'releases' : releases
    }
    
    return render(request, 'collection/index.html', context)


def release(request, id):
    
    release = Release.objects.filter(release_id=id).first()
    tracks = release.track_set.order_by('position').all()
    
    context = {
        'release' : release,
        'tracks' : tracks
    }
    
    return render(request, 'collection/release.html', context)