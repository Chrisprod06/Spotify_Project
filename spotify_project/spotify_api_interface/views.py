import httpx

from django.shortcuts import render, redirect
from django.urls import reverse

from .functions import auth_spotify, get_artist_data, get_artist_albums
from .forms import SearchArtistForm


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
    View to handle artist details retrieval and display. Get Artist, Artist's Albums
    :param artist_id:
    :param request:
    :return:
    """

    template = "spotify_api_interface/artist_details.html"
    context = {}
    access_token = auth_spotify()

    # Get artist data, albums
    artist_data = get_artist_data(artist_id, access_token)
    artist_albums = get_artist_albums(artist_id, access_token)

    print(artist_albums)
    # Prepare data for template
    context["artist_data"] = {
        "url": artist_data.get("external_urls", "").get("spotify", ""),
        "followers": artist_data.get("followers", "").get("total", ""),
        "genres": artist_data.get("genres", []),
        "id": artist_data.get("id", ""),
        "image": artist_data.get("images", [])[0].get("url", "") if len(artist_data.get("images", [])) > 1 else "",
        "name": artist_data.get("name", ""),
        "popularity": artist_data.get("popularity", 0)
    }

    return render(
        request,
        template,
        context
    )
