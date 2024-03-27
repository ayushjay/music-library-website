from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    RedirectView,
    DeleteView,
)
from .models import Folder, Song, Author, UserProfile
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from .forms import MusicForm


class SongCreateView(CreateView):
    model = Song
    form_class = MusicForm
    template_name = "music/create_post.html"
    success_url = "/songs/"


class SongListView(ListView):
    model = Song
    template_name = "music/index.html"
    fields = ["title", "audio", "date", "author", "artist", "genre"]
    paginate_by = 10


class SongDetailView(DetailView):
    model = Song
    template_name = "music/song_detail.html"


class SongDeleteView(DeleteView):
    model = Song
    template_name = "music/song_delete.html"
    success_url = reverse_lazy("music:song-list")
