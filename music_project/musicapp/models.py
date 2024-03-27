from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse


class Folder(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField("Song")

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=200)
    audio = models.FileField(upload_to="media/songdir")
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    date = models.DateTimeField(
        auto_now=True,
    )
    artist = models.TextField(max_length=200)
    genre = models.TextField()

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=100)

    def __str__(self):
        return self.last_name


class UserProfile(models.Model):
    user = models.OneToOneField(Author, on_delete=models.CASCADE)
    favorites = models.ForeignKey(
        Folder, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.user.username
