import json
import requests
from dotenv import load_dotenv
import os
import base64
from requests import post
from datetime import datetime
from definitions import CONFING_FILES

load_dotenv()
CLIENT_ID: str = os.getenv("CLIENT_ID")
CLIENT_SECRET: str = os.getenv("CLIENT_SECRET")
RAT_PARTY_MIX_ID: str = os.getenv("RAT_PARTY_MIX_ID")


# RAT_PARTY_MIX_ID: str = "7llfakgLAYwUxDhRk8lYIO"
# BOT_PATH = os.getcwd()


class Spotify:
    __instance = None
    token = None
    headers = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.token = cls.get_token()
            cls.headers = cls.get_auth_header()

            return cls.__instance
        else:
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

    @classmethod
    def get_auth_header(cls) -> dict:
        if cls.token is not None:
            return {"Authorization": "Bearer " + cls.token}
        return {}


class Song:
    # __new__ override?
    def __init__(self, added_at=None, added_by: str = None,
                 response: dict = None):
        if response is not None:
            self.song_name = response['name']
            self.spotify_id = response['id']
            self.song_link = response['external_urls']['spotify']
            self.photo_link = response['album']['images'][0]['url']
            self.popularity = response['popularity']
            self.preview_url = response['preview_url']

        if added_by is not None:
            self.added_by = added_by['id']
        if added_at is not None:
            added_at = added_at.replace("T", " ").replace("Z", "")
            self.added_at = datetime.strptime(added_at, "%Y-%m-%d %H:%M:%S")

        self.artists_list = []


class Artist:
    def __init__(self, spotify_id: str = None, artist_name: str = None, response: dict = None):
        if response is not None:
            self.spotify_id = response['id']
            self.artist_name = response['name']
            return
        self.spotify_id = spotify_id
        self.artist_name = artist_name


def get_song_by_id(song_id: str) -> Song:
    spotify_connection: Spotify = Spotify()
    url: str = f'https://api.spotify.com/v1/tracks/{song_id}'
    response: requests = requests.get(url, headers=spotify_connection.headers)
    response_json: dict = response.json()

    song_object: Song = Song(response=response_json)
    song_object.artists_list = []

    for artist in response_json['artists']:
        artist_object: Artist = Artist(response=artist)
        song_object.artists_list.append(artist_object)

    return song_object


def get_playlist_elements() -> list:
    spotify_api_connection: Spotify = Spotify()

    snapshot_url: str = f'https://api.spotify.com/v1/playlists/{RAT_PARTY_MIX_ID}?fields=snapshot_id'
    response: requests = requests.get(snapshot_url, headers=spotify_api_connection.headers)
    snapshot_response_json: dict = response.json()

    with open(os.path.join(CONFING_FILES, "snapshots_ids.json"), "r") as file:
        snapshots: list = json.load(file)

    if snapshot_response_json['snapshot_id'] == snapshots[-1]:  # no changes on playlist
        print("No changes on playlist :(")
        return []

    # reading new data

    url: str = f'https://api.spotify.com/v1/playlists/{RAT_PARTY_MIX_ID}/tracks?limit=50'

    received_songs: list = []

    while url:
        response: requests = requests.get(url, headers=spotify_api_connection.headers)
        response_json: dict = response.json()
        if response.status_code == 200:

            for track in response_json['items']:
                song_object: Song = Song(added_at=track['added_at'], added_by=track['added_by'],
                                         response=track['track'])

                for artist in track['track']['artists']:
                    artist_object: Artist = Artist(response=artist)
                    song_object.artists_list.append(artist_object)

                received_songs.append(song_object)

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
    spotify_api_connection: Spotify = Spotify()

    url: str = f'https://api.spotify.com/v1/playlists/{RAT_PARTY_MIX_ID}'
    response: requests = requests.get(url, headers=spotify_api_connection.headers)
    response_json: dict = response.json()
    print(response_json)
    description: str = response_json.get("description")
    return  description


if __name__ == "__main__":
    pass


