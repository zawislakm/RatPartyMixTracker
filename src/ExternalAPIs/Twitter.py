import json
import logging
import os
import random

import requests
import tweepy
from tweepy import TweepyException

from src.Database.models import Song
from src.Definitions.definitions import BOT_PATH, ANNOUNCEMENTS_PATH
from src.ExternalAPIs.__init__ import API_KEY_TWITTER, API_KEY_SECRET_TWITTER, BEARER_TOKEN_TWITTER, \
    ACCESS_TOKEN_TWITTER, ACCESS_TOKEN_SECRET_TWITTER

Client = tweepy.Client(BEARER_TOKEN_TWITTER, API_KEY_TWITTER, API_KEY_SECRET_TWITTER, ACCESS_TOKEN_TWITTER,
                       ACCESS_TOKEN_SECRET_TWITTER)
auth = tweepy.OAuth1UserHandler(API_KEY_TWITTER, API_KEY_SECRET_TWITTER, ACCESS_TOKEN_TWITTER,
                                ACCESS_TOKEN_SECRET_TWITTER)
API = tweepy.API(auth)
PHOTO_PATH: str = os.path.join(BOT_PATH, "temp.jpg")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
    all_songs_list = []

    for song in songs[:3]:
        artists_string = ", ".join(artist.artist_name for artist in song.get_artists())
        all_songs_list.append(f"{song.song_name} from {artists_string}")

    if len(songs) > 3:
        all_songs_list.append("AND MUCH MORE, CHECK THE PLAYLIST!")

    all_songs_string = "\n".join(all_songs_list)
    return all_songs_string


def changes_playlist_tweet(songs: list, announcement_file: str) -> None:
    # TODO move announcement to database
    with open(os.path.join(ANNOUNCEMENTS_PATH, announcement_file), "r") as file:
        announcement_texts = json.load(file)

    songs.sort(key=lambda x: x.popularity, reverse=True)

    text = random.choice(announcement_texts)
    text = text.format(get_songs_string(songs), songs[0].song_link)
    make_tweet(text, songs[0].song_photo_link)


def daily_song_tweet(song: Song) -> None:
    # TODO move announcement to database
    with open(os.path.join(ANNOUNCEMENTS_PATH, "daily_announcements.json"), "r") as file:
        daily_announcements = json.load(file)

    text = random.choice(daily_announcements)
    text = text.format(song.song_name, ", ".join(artist.artist_name for artist in song.get_artists()),
                       song.song_link)
    make_tweet(text, None)


def make_tweet(text: str, song_url: str = None) -> None:
    try:

        if song_url is not None and read_photo(song_url):
            media = API.media_upload(PHOTO_PATH)
            Client.create_tweet(text=text, media_ids=[media.media_id])
            remove_photo()
        else:
            Client.create_tweet(text=text)
    except TweepyException as e:
        logger.info(f"Error while tweeting: {e}")


if __name__ == "__main__":
    pass
