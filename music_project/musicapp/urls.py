from django.urls import path
from . import views
from .views import MyLoginView, MyLogoutView, MyRegisterView, ProfileView

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("register/", MyRegisterView.as_view(), name="register"),
    path("accounts/profile/", ProfileView.as_view(), name="profile"),
    path("accounts/login/", MyLoginView.as_view(), name="login"),
    path("", views.SongListView.as_view(), name="song-list"),
    path("song/create/", views.SongCreateView.as_view(), name="song-create"),
    path("song/<int:pk>/update/", views.SongUpdateView.as_view(), name="song-update"),
    path("song/<int:pk>/delete/", views.SongDeleteView.as_view(), name="song-delete"),
    path("songs/<int:pk>/", views.SongDetailView.as_view(), name="song-detail"),
    path("folders/", views.UserFoldersView.as_view(), name="user-folders"),
    path("folders/<int:pk>/", views.FolderDetailView.as_view(), name="folder-detail"),
    path("folder/create/", views.FolderCreateView.as_view(), name="folder-create"),
    path(
        "folder/<int:pk>/update/",
        views.FolderUpdateView.as_view(),
        name="folder-update",
    ),
    path(
        "folder/<int:pk>/delete/",
        views.FolderDeleteView.as_view(),
        name="folder-delete",
    ),
]
