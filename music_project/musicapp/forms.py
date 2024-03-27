from django import forms
from .models import Folder, Song, Author, UserProfile


class MusicForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["title", "audio", "author", "date", "artist", "genre"]
