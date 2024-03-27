from django import forms
from .models import Song, Folder


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["title", "artist", "genre", "file"]


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ["name"]
