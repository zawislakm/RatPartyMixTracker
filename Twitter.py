from dotenv import load_dotenv
import os
import tweepy
import requests

load_dotenv()

API_KEY_TWITTER = os.getenv('API_KEY_TWITTER')
API_KEY_SECRET_TWITTER = os.getenv('API_KEY_SECRET_TWITTER')
BEARER_TOKEN_TWITTER = os.getenv('BEARER_TOKEN_TWITTER')
ACCESS_TOKEN_TWITTER = os.getenv('ACCESS_TOKEN_TWITTER')
ACCESS_TOKEN_SECRET_TWITTER = os.getenv('ACCESS_TOKEN_SECRET_TWITTER')

Client = tweepy.Client(BEARER_TOKEN_TWITTER, API_KEY_TWITTER, API_KEY_SECRET_TWITTER, ACCESS_TOKEN_TWITTER,
                       ACCESS_TOKEN_SECRET_TWITTER)
auth = tweepy.OAuth1UserHandler(API_KEY_TWITTER, API_KEY_SECRET_TWITTER, ACCESS_TOKEN_TWITTER,
                                ACCESS_TOKEN_SECRET_TWITTER)
API = tweepy.API(auth)

PHOTO_PATH = "temp.jpg"


def get_artists_amount(songs: list) -> int:
    amount = 0
    for song in songs:
        amount += len(song['artists'])

    return amount


def read_photo(photo_url: str) -> bool:
    photo_request = requests.get(photo_url, stream=True)
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
        print(f"Plik {PHOTO_PATH} nie istnieje i nie może zostać usunięty.")
        return False


def removed_songs_tweet(songs: list) -> None:
    artists_amount = get_artists_amount(songs)
    if len(songs) == 1:
        text = f"{songs[0]['artists'][0]} NERFS!\n" \
               f"{songs[0]['name']} has been removed from RatPartyMix"
    else:
        text = f"{songs[0]['artists'][0]} and {artists_amount - 1} other artists NERFS!\n" \
               f"{songs[0]['name']} and {len(songs) - 1} other songs have been removed from RatPartyMix"

    make_tweet(text, songs[0]['photo_link'])


def added_songs_tweet(songs: list) -> None:
    artists_amount = get_artists_amount(songs)

    if len(songs) == 1:
        text = f"{songs[0]['artists'][0]} BUFFS!\n" \
               f"{songs[0]['name']} has been added to RatPartyMix\n" \
               f"LISTEN NOW!\n" \
               f"{songs[0]['song_link']}"
    else:
        text = f"{songs[0]['artists'][0]} and {artists_amount - 1} other artists BUFFS!\n" \
               f"{songs[0]['name']} and {len(songs) - 1} other songs have been added to RatPartyMix\n" \
               f"LISTEN NOW!\n" \
               f"{songs[0]['song_link']}"

    make_tweet(text, songs[0]['photo_link'])


def daily_song_tweet(song: dict) -> None:
    text = f"Turn on JBLs!\n" \
           f"{song['name']} from {song['artists'][0]} is your daily song\n" \
           f"LISTEN NOW!\n" \
           f"{song['song_link']}"

    make_tweet(text, song['photo_link'])


def make_tweet(text: str, song_url: str) -> None:
    if read_photo(song_url):
        media = API.media_upload(PHOTO_PATH)
        Client.create_tweet(text=text, media_ids=[media.media_id])
        remove_photo()
    else:
        Client.create_tweet(text=text)


if __name__ == "__main__":
    pass

    # Client.create_tweet(text="Hello Pitbull!\n Test Here!")
