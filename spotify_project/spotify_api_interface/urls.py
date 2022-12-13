from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search_artist", views.search_artist, name="search-artist"),
    path("search_albums", views.search_albums, name="search-albums"),
    path("view_artist_details/<str:artist_id>", views.view_artist_details, name="view-artist-details"),
    path("view_artist_albums/<str:artist_id>/<int:number_of_albums>", views.view_artist_albums,
         name="view-artist-albums")
]
