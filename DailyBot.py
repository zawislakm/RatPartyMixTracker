import Spotify
import Twitter
import random

if __name__ == "__main__":
    # go once per day
    token = Spotify.get_token()
    songs_list = Spotify.load_data_new()
    random_song_id = random.choice(songs_list)
    song_dict = Spotify.get_song_by_id(random_song_id,token)
    Twitter.daily_song_tweet(song_dict)
