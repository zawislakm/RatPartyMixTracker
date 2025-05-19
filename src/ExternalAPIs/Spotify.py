import base64
import datetime
import json

import requests
from requests import post

from src.Database.models import Song, Artist
from src.ExternalAPIs.__init__ import CLIENT_ID, CLIENT_SECRET, RAT_PARTY_MIX_ID


class Spotify:
    __instance = None
    __access_token = None
    __expires_in = None
    __authorization_header = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            auth_string = CLIENT_ID + ":" + CLIENT_SECRET
            auth_bytes = auth_string.encode("utf-8")
            auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
            cls.__authorization_header = {
                "Authorization": f'Basic {auth_base64}',
                "Content-Type": "application/x-www-form-urlencoded"
            }
        return cls.__instance

    @classmethod
    def set_access_token(cls):
        url = 'https://accounts.spotify.com/api/token'
        data = {'grant_type': 'client_credentials'}
        result = post(url, headers=cls.__authorization_header, data=data)
        if result.status_code != 200:
            raise Exception(f"Failed to get authorization token from Spotify with code: {result.status_code}")
        json_result = json.loads(result.content)
        token = json_result['access_token']
        cls.__expires_in = datetime.datetime.now().timestamp() + json_result['expires_in'] - 60
        cls.__access_token = {"Authorization": "Bearer " + json_result['access_token']}
        return token

    @property
    def auth_headers(self) -> dict:
        if self.__access_token is None or datetime.datetime.now().timestamp() > self.__expires_in:
            self.set_access_token()
        return self.__access_token


SPOTIFY_CONNECTION = Spotify()


def get_song_by_id(song_id: str) -> Song | None:
    url = f'https://api.spotify.com/v1/tracks/{song_id}'
    response = requests.get(url, headers=SPOTIFY_CONNECTION.auth_headers)
    if response.status_code != 200:
        print(f"Failed to get song by id: {response.status_code}")
        return None
    response_json = response.json()

    song = Song(data=response_json)

    for artist in response_json['artists']:
        artist = Artist(data=artist)
        song.add_artist(artist)

    return song


def get_playlist_current_snapshot() -> str | None:
    url = f'https://api.spotify.com/v1/playlists/{RAT_PARTY_MIX_ID}?fields=snapshot_id'
    response = requests.get(url, headers=SPOTIFY_CONNECTION.auth_headers)
    if response.status_code != 200:
        print(f"Failed to get playlist snapshot id: {response.status_code}")
        return None

    response_json = response.json()
    return response_json['snapshot_id']


def get_playlist_elements() -> list:
    # reading new data
    url = f'https://api.spotify.com/v1/playlists/{RAT_PARTY_MIX_ID}/tracks?limit=50'

    received_songs = []

    while url:
        response = requests.get(url, headers=SPOTIFY_CONNECTION.auth_headers)
        response_json = response.json()
        if response.status_code == 200:

            for track in response_json['items']:
                song = Song(added_at=track['added_at'], added_by=track['added_by'], data=track['track'])

                for artist in track['track']['artists']:
                    artist = Artist(data=artist)
                    song.add_artist(artist)

                received_songs.append(song)

            url = response_json['next']

        else:
            # End of requests
            break

    return received_songs


def get_playlist_description() -> str:
    url = f'https://api.spotify.com/v1/playlists/{RAT_PARTY_MIX_ID}'
    response = requests.get(url, headers=SPOTIFY_CONNECTION.auth_headers)
    response_json = response.json()
    description = response_json["description"]
    return description


if __name__ == "__main__":
    pass
