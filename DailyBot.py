import Database as db
import Spotify
import Twitter


def random_song() -> None:
    daily_song = db.get_daily_song()

    song_object = Spotify.get_song_by_id(daily_song.spotify_id)
    Twitter.daily_song_tweet(song_object)


if __name__ == "__main__":
    random_song()
