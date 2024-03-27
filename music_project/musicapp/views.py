from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    RedirectView,
    DeleteView,
    UpdateView,
)
from .models import Folder, Song
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse, render
from django.urls import reverse_lazy
from .forms import SongForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "musicapp/profile.html"


class MyLoginView(LoginView):
    template_name = "musicapp/login.html"


class MyLogoutView(LogoutView):
    next_page = "musicapp/login"


class MyRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "musicapp/register.html"
    success_url = reverse_lazy("login")


class SongListView(ListView):
    model = Song
    template_name = "musicapp/song_list.html"
    fields = ["title", "artist", "genre", "file"]
    paginate_by = 10
    context_object_name = "song_list"


class SongCreateView(LoginRequiredMixin, CreateView):
    model = Song
    form_class = SongForm
    template_name = "musicapp/song_form.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class SongDetailView(LoginRequiredMixin, DetailView):
    model = Song
    template_name = "musicapp/song_detail.html"


class SongUpdateView(LoginRequiredMixin, UpdateView):
    model = Song
    template_name = "musicapp/song_form.html"
    fields = ["title", "artist", "genre", "file"]
    success_url = reverse_lazy("song-list")


class SongDeleteView(LoginRequiredMixin, DeleteView):
    model = Song
    template_name = "musicapp/song_confirm_delete.html"
    success_url = reverse_lazy("song-list")


class UserFoldersView(LoginRequiredMixin, ListView):
    model = Folder
    template_name = "musicapp/user_folders.html"
    context_object_name = "folders"

    def get_queryset(self):
        # Filter folders by the logged-in user
        return Folder.objects.filter(owner=self.request.user)


class FolderCreateView(LoginRequiredMixin, CreateView):
    model = Folder
    template_name = "musicapp/folder_form.html"
    fields = ["name"]
    success_url = reverse_lazy("user-folders")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class FolderUpdateView(LoginRequiredMixin, UpdateView):
    model = Folder
    fields = ["name"]  # Add other fields as needed
    template_name = "musicapp/folder_form.html"
    success_url = "/folders/"


class FolderDetailView(LoginRequiredMixin, DetailView):
    model = Folder
    template_name = "musicapp/folder_detail.html"


class FolderDeleteView(LoginRequiredMixin, DeleteView):
    model = Folder
    success_url = reverse_lazy("user-folders")
