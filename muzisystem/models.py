from __future__ import unicode_literals

from django.db import models
from datetime import date


def url_track_thumbnail(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.track_name, ext)
    return "{id}/thumbnails/{file}".format(id=instance.album_id.album_name, file=filename)


def url_track(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.track_name, ext)
    return "{id}/{file}".format(id=instance.album_id.album_name, file=filename)


def url_album_thumbnail(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.album_name, ext)
    return "{id}/thumbnails/{file}".format(id=instance.album_name, file=filename)


def url_artist(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.artist_name, ext)
    return "artists/{file}".format(file=filename)


class Artists(models.Model):
    artist_name = models.CharField(max_length=250)
    artist_description = models.CharField(max_length=1000)
    artist_picture = models.ImageField(upload_to=url_artist)

    def __str__(self):
        return self.artist_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=250)
    genre_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.genre_name


class Albums(models.Model):
    artist_id = models.ForeignKey('Artists', on_delete=models.CASCADE)
    album_name = models.CharField(max_length=250)
    album_releasedate = models.DateField(default=date.today)
    genre_id = models.ForeignKey('Genre')
    album_thumbnail = models.FileField(upload_to=url_album_thumbnail)

    def __str__(self):
        return self.album_name + ' ( ' + self.artist_id.artist_name + ' ) '


class Tracks(models.Model):
    album_id = models.ForeignKey('Albums', on_delete=models.CASCADE)
    track_name = models.CharField(max_length=250)
    track_thumbnail = models.ImageField(upload_to=url_track_thumbnail, blank=True)
    track = models.FileField(upload_to=url_track)

    def __str__(self):
        return self.track_name + ' ( ' + self.album_id.album_name + ' ) '

