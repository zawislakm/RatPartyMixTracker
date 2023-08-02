import Spotify
import Twitter
import random
import Database


def random_song():
    db: Database.DatabaseConnection = Database.DatabaseConnection()
    spotify_id: str = Database.get_daily_song_database()

    song_object: Spotify.Song = Spotify.get_song_by_id(spotify_id)
    Twitter.daily_song_tweet(song_object)

    db.close_connection()


if __name__ == "__main__":
    # go once per day
    random_song()

    # token = Spotify.get_token()
    # songs_list = Spotify.load_data_new()
    # random_song_id = random.choice(songs_list)
    # song_dict = Spotify.get_song_by_id(random_song_id, token)
    # Twitter.daily_song_tweet(song_dict)
