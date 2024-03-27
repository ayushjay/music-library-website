from django.contrib import admin
from django.urls import path, include
from .views import (
    SongCreateView,
    SongDetailView,
    SongListView,
    SongDeleteView,
)
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"

urlpatterns = [
    path("", RedirectView.as_view(url="http://localhost:8000/songs/"), name="home"),
    path("songs/", SongListView.as_view(), name="song-list"),
    path("create/", SongCreateView.as_view(), name="song-create"),
    path("songs/<int:pk>", SongDetailView.as_view(), name="song-detail"),
    path("delete/<int:pk>/", SongDeleteView.as_view(), name="song-delete"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
