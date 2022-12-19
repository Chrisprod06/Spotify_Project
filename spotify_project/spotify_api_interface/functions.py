from math import ceil

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
    clean_artist_data = {}
    try:
        url = f"https://api.spotify.com/v1/artists/{artist_id}"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = httpx.get(url, headers=headers)
        artist_data = response.json()

        clean_artist_data = {
            "url": artist_data.get("external_urls", "").get("spotify", ""),
            "followers": artist_data.get("followers", "").get("total", ""),
            "genres": artist_data.get("genres", []),
            "id": artist_data.get("id", ""),
            "image": artist_data.get("images", [])[0].get("url", "") if len(artist_data.get("images", [])) > 1 else "",
            "name": artist_data.get("name", ""),
            "popularity": artist_data.get("popularity", 0)
        }

    except httpx.TimeoutException as error:
        print(f"GET artist API timeout error: {error}")
    except httpx.NetworkError as error:
        print(f"GET artist API network error: {error}")
    except Exception as error:
        print(f"GET artist API error: {error}")
    return clean_artist_data


def get_album_data(artist_id, access_token, number_of_albums):
    """
    Function to get details of an artist albums
    :param number_of_albums:
    :param artist_id:
    :param access_token:
    :return:
    """
    # Get artist albums
    clean_artist_albums = []
    try:
        url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        params = {"limit": number_of_albums}
        response = httpx.get(url, headers=headers, params=params)
        response_data = response.json()

        # Get items from response_data
        items = response_data.get("items", [])

        if items:
            for item in items:
                album_name = item.get("name", "")
                # If album name is too big, slice for a cleaner look in html
                if len(album_name) > 28:
                    album_name = f"{album_name[0:28]}.."
                clean_artist_albums.append({
                    "album_id": item.get("id", 0),
                    "image": item.get("images", [])[1].get("url", ""),
                    "name": album_name,
                    "release_date": item.get("release_date", ""),
                    "total_tracks": item.get("total_tracks", 0)
                })

        return clean_artist_albums
    except httpx.TimeoutException as error:
        print(f"GET artist albums API timeout error: {error}")
    except httpx.NetworkError as error:
        print(f"GET artist albums API network error: {error}")
    except Exception as error:
        print(f"GET artist albums API error: {error}")
    return clean_artist_albums


def get_album_tracks(album_id, access_token):
    """
    Function to get tracks of requested album
    :param album_id:
    :param access_token:
    :return:
    """
    try:
        url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        response = httpx.get(url, headers=headers, )
        response_data = response.json()
        # Clean data
        clean_album_tracks = []
        items = response_data.get("items", "")
        print(items[0])
        if items:
            for item in items:
                clean_album_tracks.append({
                    "disc_number": item.get("disc_number", 0),
                    "duration": item.get("duration", 0),
                    "explicit": item.get("explicit", False),
                    "spotify_url": ""
                })


    except httpx.TimeoutException as error:
        print(f"GET artist albums API timeout error: {error}")
    except httpx.NetworkError as error:
        print(f"GET artist albums API network error: {error}")
    except Exception as error:
        print(f"GET artist albums API error: {error}")