from django.shortcuts import render

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

    return render(
        request,
        template,
        context
    )


def display_artist_details(request):
    """
    View to handle artist details retrieval and display
    :param request:
    :return:
    """