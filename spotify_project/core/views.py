from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Default view when launching the project. Serves as a map to the rest of the application
    :param request:
    :return:
    """

    template = "index.html"
    context = {}

    return render(
        request,
        template,
        context
    )

