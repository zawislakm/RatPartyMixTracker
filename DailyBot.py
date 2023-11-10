import Database
import Spotify
import Twitter


def random_song() -> None:
    db: Database.DatabaseConnection = Database.DatabaseConnection()
    spotify_id: str = Database.get_daily_song_database()

    song_object: Spotify.Song = Spotify.get_song_by_id(spotify_id)
    Twitter.daily_song_tweet(song_object)

    db.close_connection()


if __name__ == "__main__":
    random_song()
