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
        print(response_data)
        # Get items from response_data
        items = response_data.get("items", [])
        if items:
            for item in items:
                clean_artist_albums.append({
                    "url": item.get("href", ""),
                    "image": item.get("images", [])[1].get("url", ""),
                    "name": item.get("name", ""),
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
