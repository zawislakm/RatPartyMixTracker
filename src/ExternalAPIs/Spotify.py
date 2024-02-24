import base64
import json
import os

import requests
from requests import post

from src.Database.models import Song, Artist
from src.Definitions.definitions import CONFING_FILES
from src.ExternalAPIs.__init__ import CLIENT_ID, CLIENT_SECRET, RAT_PARTY_MIX_ID


class Spotify:
    __instance = None
    token = None
    headers = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.headers = {"Authorization": "Bearer " + cls.get_token()}

        return cls.__instance

    @classmethod
    def get_token(cls) -> str:
        auth_string = CLIENT_ID + ":" + CLIENT_SECRET
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

        url = 'https://accounts.spotify.com/api/token'
        headers = {
            "Authorization": f'Basic {auth_base64}',
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {'grant_type': 'client_credentials'}
        result = post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        token = json_result['access_token']
        return token


SPOTIFY_CONNECTION = Spotify()


def get_song_by_id(song_id: str) -> Song:
    url = f'https://api.spotify.com/v1/tracks/{song_id}'
    response = requests.get(url, headers=SPOTIFY_CONNECTION.headers)
    response_json = response.json()

    song = Song(data=response_json)

    for artist in response_json['artists']:
        artist = Artist(data=artist)
        song.add_artist(artist)

    return song


def get_playlist_elements() -> list:
    snapshot_url = f'https://api.spotify.com/v1/playlists/{RAT_PARTY_MIX_ID}?fields=snapshot_id'
    response = requests.get(snapshot_url, headers=SPOTIFY_CONNECTION.headers)
    snapshot_response_json = response.json()

    with open(os.path.join(CONFING_FILES, "snapshots_ids.json"), "r") as file:
        snapshots = json.load(file)

    if snapshot_response_json['snapshot_id'] == snapshots[-1]:  # no changes on playlist
        print("No changes on playlist :(")
        return []

    # reading new data

    url = f'https://api.spotify.com/v1/playlists/{RAT_PARTY_MIX_ID}/tracks?limit=50'

    received_songs = []

    while url:
        response = requests.get(url, headers=SPOTIFY_CONNECTION.headers)
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

    # saving snapshot after successfully requesting data
    snapshots.append(snapshot_response_json['snapshot_id'])
    with open(os.path.join(CONFING_FILES, "snapshots_ids.json"), "w") as file:
        json.dump(snapshots, file)

    return received_songs


def get_playlist_description() -> str:
    url = f'https://api.spotify.com/v1/playlists/{RAT_PARTY_MIX_ID}'
    response = requests.get(url, headers=SPOTIFY_CONNECTION.headers)
    response_json = response.json()
    description = response_json["description"]
    return description


if __name__ == "__main__":
    pass
