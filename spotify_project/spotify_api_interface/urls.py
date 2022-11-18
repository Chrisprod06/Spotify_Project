from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search_artist", views.search_artist, name="search-artist")
]
