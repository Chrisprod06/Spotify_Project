import httpx

from django.shortcuts import render, redirect
from django.urls import reverse

from .functions import auth_spotify, get_artist_data, get_album_data, get_album_tracks
from .forms import SearchArtistForm, SearchAlbumsForm


def index(request):
    """
    Home page view of the project
    :param request:
    :return:
    """
    template = "spotify_api_interface/index.html"
    context = {}

    return render(
        request,
        template,
        context
    )


def search_artist(request):
    """
    View to handle artist lookup
    :param request:
    :return:
    """

    template = "spotify_api_interface/search_artist.html"
    context = {}

    form = SearchArtistForm()

    context["form"] = form

    if request.method == "POST":
        form = SearchArtistForm(request.POST)
        if form.is_valid():
            artist_id = form.cleaned_data["artist_id"]
            return redirect(reverse('view-artist-details', kwargs={'artist_id': artist_id}))

    return render(
        request,
        template,
        context
    )


def view_artist_details(request, artist_id):
    """
    View to handle artist details retrieval and display.
    :param artist_id:
    :param request:
    :return:
    """

    template = "spotify_api_interface/artist_details.html"
    context = {}
    access_token = auth_spotify()

    # Get artist data
    artist_data = get_artist_data(artist_id, access_token)

    # Prepare data for template
    context["artist_data"] = artist_data

    return render(
        request,
        template,
        context
    )


def search_albums(request):
    """
    View to handle artist lookup
    :param request:
    :return:
    """

    template = "spotify_api_interface/search_albums.html"
    context = {}

    form = SearchAlbumsForm()

    context["form"] = form

    if request.method == "POST":
        form = SearchAlbumsForm(request.POST)
        if form.is_valid():
            artist_id = form.cleaned_data["artist_id"]
            number_of_albums = form.cleaned_data["number_of_albums"]
            return redirect(
                reverse("view-artist-albums", kwargs={"artist_id": artist_id, "number_of_albums": number_of_albums}))

    return render(
        request,
        template,
        context
    )


def view_artist_albums(request, artist_id, number_of_albums):
    """
    View to handle artist albums retrieval and display.
    :param number_of_albums:
    :param request:
    :param artist_id:
    :return:
    """
    template = "spotify_api_interface/artist_albums.html"
    context = {}
    access_token = auth_spotify()

    # Get album data
    album_data = get_album_data(artist_id, access_token, number_of_albums)

    # Prepare data for template
    context["album_data"] = album_data
    return render(
        request,
        template,
        context
    )


def view_album_tracks(request, album_id):
    """
    View to handle album tracks retrieval and display.
    :param request:
    :param album_id:
    :return:
    """
    template = "spotify_api_interface/album_tracks.html"
    context = {}
    access_token = auth_spotify()

    # Get album tracks
    album_tracks = get_album_tracks(album_id, access_token)

    # Prepare data for template
    context["album_tracks"] = album_tracks
    return render(
        request,
        template,
        context
    )