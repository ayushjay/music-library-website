from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from django.contrib.auth.models import User


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    file = models.FileField(upload_to="music_tracks/", default="sampleHappyMusic.mp3")


class Folder(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    songs = models.ManyToManyField(Song)
