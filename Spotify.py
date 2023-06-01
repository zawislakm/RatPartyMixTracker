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

RAT_PARTY_MIX_ID = os.getenv("RAT_PARTY_MIX_ID")

# RAT_PARTY_MIX_ID = "7llfakgLAYwUxDhRk8lYIO"
BOT_PATH = os.getenv("BOT_PATH")


def get_auth_header(token: str) -> dict:
    return {"Authorization": "Bearer " + token}


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


def load_data_new() -> list:
    with open(BOT_PATH + "song_ids.json", "r") as f:
        return json.load(f)


def save_data_new(songs: list) -> None:
    to_save = []
    for song in songs:
        to_save.append(song['track']['id'])

    with open(BOT_PATH + "song_ids.json", "w+") as f:
        json.dump(to_save, f)


def get_song_by_id(song_id: str, token: str) -> dict:
    headers = get_auth_header(token)
    url = f'https://api.spotify.com/v1/tracks/{song_id}'
    response = requests.get(url, headers=headers)
    response_json = response.json()

    artist_list = []
    for artist in response_json['artists']:
        artist_list.append(artist['name'])

    small_dict = {
        'name': response_json['name'],  # Song name
        'artists': artist_list,  # Artists list
        'song_link': response_json['external_urls']['spotify'],  # Song spotify link
        'photo_link': response_json['album']['images'][0]['url'],  # Song photo
        'popularity': response_json['popularity']  # Song popularity
    }

    return small_dict


def get_removed_songs(old_data: list, new_data: list, token: str) -> list:
    removed_song_ids = []
    for song_old_id in old_data:
        for song_new in new_data:
            if song_old_id == song_new['track']['id']:
                break
        else:
            removed_song_ids.append(song_old_id)

    song_list = []
    for found_id in removed_song_ids:
        song_list.append(get_song_by_id(found_id, token))
    song_list.sort(key=lambda x: x['popularity'], reverse=True)

    return song_list


def get_added_songs(old_data: list, new_data: list) -> list:
    song_list = []
    for song_new in new_data:
        if song_new['track']['id'] not in old_data:
            song_list.append(song_new)

    return get_song_list_to_small_dict(song_list)


def song_dict_small(song: dict) -> dict:
    artist_list = []
    for artist in song['track']['artists']:
        artist_list.append(artist['name'])
    song_dict = {
        'name': song['track']['name'],  # Song name
        'artists': artist_list,  # Artists list
        'song_link': song['track']['external_urls']['spotify'],  # Song spotify link
        'photo_link': song['track']['album']['images'][0]['url'],  # Song photo
        'popularity': song['track']['popularity']  # Song popularity
    }
    return song_dict


def get_song_list_to_small_dict(songs: list) -> list:
    info = []
    for song in songs:
        info.append(song_dict_small(song))

    info.sort(key=lambda x: x['popularity'], reverse=True)

    return info


def work_script() -> (list, list):
    token = get_token()
    new_data_big_json = get_playlist_elements(token)
    old_data_songs_ids = load_data_new()

    removed = get_removed_songs(old_data_songs_ids, new_data_big_json, token)
    added = get_added_songs(old_data_songs_ids, new_data_big_json)

    save_data_new(new_data_big_json)
    return removed, added


if __name__ == "__main__":
    pass

    # removed, added = work_script()
    #
    # print("Added:")
    # print(added)
    #
    # print()
    #
    # print("Removed")
    # print(removed)
    # token = get_token()
    # get_song_by_id("2UKvxuMTM7JwprZrnpxgY1",token)

    # token = get_token()
    # new_data = get_playlist_elements(token)
    # old_data = load_data_new()
    # #
    # removed = get_removed_songs_new(old_data, new_data, token)
    # added = get_added_songs_new(old_data, new_data)
    # print("Removed: ")
    # print(removed)
    # print(len(removed))
    #
    # print()
    #
    # print("Added: ")
    # print(added)
    # print(len(added))
    #
    # save_data_new(new_data)
