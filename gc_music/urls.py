from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('songs', views.songs, name='songs'),
    path('song/<int:id>', views.song, name='song'),
    path('new_song', views.new_song, name="New Song")
]
