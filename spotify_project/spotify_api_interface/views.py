import httpx

from django.shortcuts import render, redirect
from django.urls import reverse

from .functions import auth_spotify
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
    View to handle artist details retrieval and display
    :param artist_id:
    :param request:
    :return:
    """

    template = "spotify_api_interface/artist_details.html"
    context = {}
    artist_data = {}
    print(artist_id)
    try:
        access_token = auth_spotify()
        url = f"https://api.spotify.com/v1/artists/{artist_id}"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = httpx.get(url, headers=headers)
        artist_data = response.json()
        
    except httpx.TimeoutException as error:
        print(f"GET artist API timeout error: {error}")
    except httpx.NetworkError as error:
        print(f"GET artist API network error: {error}")
    except Exception as error:
        print(f"GET artist API error: {error}")

    context["artist_data"] = artist_data

    return render(
        request,
        template,
        context
    )
