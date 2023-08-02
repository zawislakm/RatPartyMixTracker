from dotenv import load_dotenv
import os
import tweepy
import requests
import json
import random
import Spotify

load_dotenv()

API_KEY_TWITTER: str = os.getenv('API_KEY_TWITTER')
API_KEY_SECRET_TWITTER: str = os.getenv('API_KEY_SECRET_TWITTER')
BEARER_TOKEN_TWITTER: str = os.getenv('BEARER_TOKEN_TWITTER')
ACCESS_TOKEN_TWITTER: str = os.getenv('ACCESS_TOKEN_TWITTER')
ACCESS_TOKEN_SECRET_TWITTER: str = os.getenv('ACCESS_TOKEN_SECRET_TWITTER')

Client = tweepy.Client(BEARER_TOKEN_TWITTER, API_KEY_TWITTER, API_KEY_SECRET_TWITTER, ACCESS_TOKEN_TWITTER,
                       ACCESS_TOKEN_SECRET_TWITTER)
auth = tweepy.OAuth1UserHandler(API_KEY_TWITTER, API_KEY_SECRET_TWITTER, ACCESS_TOKEN_TWITTER,
                                ACCESS_TOKEN_SECRET_TWITTER)
API = tweepy.API(auth)
BOT_PATH: str = os.getcwd()
PHOTO_PATH: str = os.path.join(BOT_PATH, "temp.jpg")


def read_photo(get_url: str) -> bool:
    photo_request = requests.get(get_url, stream=True)
    if photo_request.status_code == 200:
        with open(PHOTO_PATH, "wb") as image:
            for chunk in photo_request:
                image.write(chunk)

        return True

    return False


def remove_photo() -> bool:
    try:
        os.remove(PHOTO_PATH)
        return True
    except FileNotFoundError:
        print(f"Image {PHOTO_PATH} doesn't exist and cannot be removed")
        return False


def get_songs_string(songs: list) -> str:
    all_songs_list: list = []

    for song in songs:
        artists_string: str = ", ".join(artist.artist_name for artist in song.artists_list)
        all_songs_list.append(f"{song.song_name} from {artists_string}")

    all_songs_string: str = "\n".join(all_songs_list)
    return all_songs_string


def changes_playlist_tweet(songs: list, announcement_path: str) -> None:
    with open(os.path.join(BOT_PATH, announcement_path), "r") as file:
        announcement_texts: list = json.load(file)

    songs.sort(key=lambda x: x.popularity, reverse=True)

    text: str = random.choice(announcement_texts)
    text: str = text.format(get_songs_string(songs), songs[0].song_link)

    make_tweet(text, songs[0].photo_link)


def daily_song_tweet(song: Spotify.Song) -> None:
    with open(os.path.join(BOT_PATH, "daily_announcements.json"), "r") as file:
        daily_announcements = json.load(file)

    text: str = random.choice(daily_announcements)
    text: str = text.format(song.song_name, ", ".join(artist.artist_name for artist in song.artists_list),
                            song.song_link)

    make_tweet(text, song.photo_link)


def make_tweet(text: str, song_url: str) -> None:
    if read_photo(song_url):
        media = API.media_upload(PHOTO_PATH)
        # Client.create_tweet(text=text, media_ids=[media.media_id])
        remove_photo()
    else:
        Client.create_tweet(text=text)


if __name__ == "__main__":
    pass
