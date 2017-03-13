from django import forms
from .models import *


class TrackForm(forms.ModelForm):
    class Meta:
        model = Tracks
        fields = ('album_id', 'track_name', 'track_thumbnail', 'track',)


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = ('artist_id', 'album_name', 'album_releasedate', 'genre_id', 'album_thumbnail',)


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artists
        fields = ('artist_name', 'artist_description', 'artist_picture',)


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('genre_name', 'genre_description',)
