from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.views.decorators.http import require_http_methods
import json

from .models import Song

# Create your views here.
def main(request):
    return HttpResponse("My Music API")

def songs(request):
    songs_list = Song.objects.all().order_by('id')
    songs = json.loads(serialize('json', songs_list))

    return JsonResponse({"songs": songs})

def song(request, id):
    song_obj = Song.objects.all().filter(id=id)
    song = json.loads(serialize('json', song_obj))

    return JsonResponse(song[0])

@require_http_methods(["POST"])
def new_song(request):
    data = request.POST

    songname = data.get('songname')
    songartist = data.get('songartist')
    songimg = data.get('songimg')
    
    mysong = Song(songname=songname, songartist=songartist, songimg=songimg)
    mysong.save()

    return HttpResponse("Song Saved")

