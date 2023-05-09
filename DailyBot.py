import Spotify
import Twitter
import random

if __name__ == "__main__":
    songs_list = Spotify.load_data()

    random_song = random.choice(songs_list)

    song_dict = Spotify.song_dict_small(random_song)

    Twitter.daily_song_tweet(song_dict)
