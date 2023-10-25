from django.shortcuts import render
from .models import *


def SongListView(request):
    songs_all = Song.objects.all()
    context = {
        'songs': songs_all
    }
    return render(request=request, template_name='song_list_template.html', context=context)


def SongDetailView(request, song_id):
    song = Song.objects.get(id=song_id)
    context = {
        'song': song
    }
    return render(request=request, template_name='song_detail_template.html', context=context)


def SongFilterView(request, genre):
    songs = Song.objects.filter(genre=genre)
    context = {
        'songs': songs
    }
    return render(request=request, template_name='song_filter_template.html', context=context)
