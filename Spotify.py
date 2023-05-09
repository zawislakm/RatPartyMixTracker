import json
from time import sleep

import requests
from dotenv import load_dotenv
import os
import base64
from requests import post

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# RAT_PARTY_MIX_ID = os.getenv("RAT_PARTY_MIX_ID")

RAT_PARTY_MIX_ID = "7llfakgLAYwUxDhRk8lYIO"


def get_token() -> str:
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


def load_data() -> list:
    with open("data.json", "r") as f:
        return json.load(f)


def save_data(songs: list) -> None:
    with open("data.json", "w+") as f:
        json.dump(songs, f)


def get_auth_header(token: str):
    return {"Authorization": "Bearer " + token}


def get_removed_songs(old_data: list, new_data: list) -> list:
    return [d for d in old_data if d not in new_data]


def get_added_songs(old_data: list, new_data: list) -> list:
    return [d for d in new_data if d not in old_data]


def get_playlist_elements(token: str) -> list:
    headers = get_auth_header(token)

    url = f'https://api.spotify.com/v1/playlists/{RAT_PARTY_MIX_ID}/tracks?limit=50'
    response = requests.get(url, headers=headers)
    response_json = response.json()

    songs = []

    while response_json['next'] is not None:
        for track in response_json['items']:
            songs.append(track)

        # Przejście do kolejnej strony
        url = response_json['next']
        response = requests.get(url, headers=headers)
        response_json = response.json()
    else:
        # osotania strona
        for track in response_json['items']:
            songs.append(track)

    return songs


def song_dict_small(song: dict) -> dict:
    artist_list = []
    for artist in song['track']['artists']:
        artist_list.append(artist['name'])
    song_dict = {
        'name': song['track']['name'],  # Nazwa utworu
        'artists': artist_list,  # Lista wykonawców
        'song_link': song['track']['external_urls']['spotify'],  # Link do utworu w serwisie Spotify
        'photo_link': song['track']['album']['images'][0]['url'],  # Link do zdjęcia okładki albumu
        'popularity': song['track']['popularity']  # Popularność utworu
    }
    return song_dict


def get_from_list(songs: list) -> list:
    info = []
    for song in songs:
        info.append(song_dict_small(song))

    info.sort(key=lambda x: x['popularity'], reverse=True)

    return info


def work_script() -> (list, list):
    token = get_token()
    new_data = get_playlist_elements(token)
    old_data = load_data()

    removed = get_removed_songs(old_data, new_data)
    added = get_added_songs(old_data, new_data)

    removed_ready = get_from_list(removed)
    added_ready = get_from_list(added)
    save_data(new_data)

    return removed_ready, added_ready


if __name__ == "__main__":
    pass
