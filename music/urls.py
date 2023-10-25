from django.urls import path
from .views import *

urlpatterns = [
    path('songs', SongListView, name='song_list_url'),
    path('song/<int:song_id>', SongDetailView, name='song_detail_url'),
    path('song/<str:genre>', SongFilterView, name='song_filter_url'),
]
