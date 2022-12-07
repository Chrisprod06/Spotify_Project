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
