from django import forms


class SearchArtistForm(forms.Form):
    """
    Form to search artist with Artist ID
    """

    artist_id = forms.CharField(max_length=255)


class SearchAlbumsForm(forms.Form):
    """
    Form to search artist with Artist ID
    """

    artist_id = forms.CharField(max_length=255)
    number_of_albums = forms.IntegerField(max_value=50)
