from django.shortcuts import render, redirect
from .models import Albums, Tracks
from .forms import *


def home(request):
    return render(request, 'testing.html', {'Albums': Albums.objects.all(), 'Tracks': Tracks.objects.all()})

def upload_track(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('muzisystem:home')
    else:
        form = TrackForm()
    return render(request, 'model_form_upload.html', {
        'form': form})

def upload_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('muzisystem:home')
    else:
        form = AlbumForm()
    return render(request, 'model_form_upload.html', {'form': form})

def upload_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('muzisystem:home')
    else:
        form = GenreForm()
    return render(request, 'model_form_upload.html', {'form': form})

def upload_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('muzisystem:home')
    else:
        form = ArtistForm()
    return render(request, 'model_form_upload.html', {'form': form})
