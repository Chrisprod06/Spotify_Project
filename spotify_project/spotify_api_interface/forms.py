from django import forms


class SearchArtistForm(forms.Form):
    """
    Form to search artist with Artist ID
    """

    artist_id = forms.CharField(max_length=255)
