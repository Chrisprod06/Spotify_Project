import httpx
from .secrets import client_secret, client_id


def auth_spotify():
    """
    Function used to authenticate spotify
    :return:
    """
    try:
        url = "https://accounts.spotify.com/api/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret
        }
        response = httpx.post(url, data=data)
        access_token = response.json().get("access_token")
        return access_token
    except httpx.TimeoutException as error:
        print(f"Auth API timeout error: {error}")
    except httpx.NetworkError as error:
        print(f"Auth API network error: {error}")
    except Exception as error:
        print(f"Auth API error: {error}")
    return


def get_artist_data(artist_id, access_token):
    """
    Function to get details of an artist
    :param artist_id:
    :param access_token:
    :return:
    """
    # Get artist data
    artist_data = {}
    try:
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
    return artist_data


def get_artist_albums(artist_id, access_token):
    """
    Function to get details of an artist albums
    :param artist_id:
    :param access_token:
    :return:
    """
    # Get artist albums
    artist_albums = {}
    try:
        url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        params = {"limit": 4}
        response = httpx.get(url, headers=headers, params=params)
        artist_albums = response.json()
    except httpx.TimeoutException as error:
        print(f"GET artist albums API timeout error: {error}")
    except httpx.NetworkError as error:
        print(f"GET artist albums API network error: {error}")
    except Exception as error:
        print(f"GET artist albums API error: {error}")
    return artist_albums
