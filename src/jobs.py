import logging

from src.Database import Database as db
from src.ExternalAPIs import Spotify, Twitter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def post_daily_song() -> None:
    daily_song = db.get_daily_song()

    song_object = Spotify.get_song_by_id(daily_song.spotify_id)
    Twitter.daily_song_tweet(song_object)


def get_song_list_from_id(songs: set) -> list:
    return list(map(lambda x: Spotify.get_song_by_id(x), songs))


def check_update() -> None:
    logger.info("Checking for updates...")
    current_snapshot = Spotify.get_playlist_current_snapshot()
    if db.check_if_current_snapshot_in_db(current_snapshot):
        logger.info("No updates on playlist")
        return

    playlist_api_result = Spotify.get_playlist_elements()

    old_songs = db.get_songs_spotify_ids()

    new_songs = set(map(lambda x: x.spotify_id, playlist_api_result))

    added_songs = new_songs - old_songs
    removed_songs = old_songs - new_songs

    if added_songs:
        logger.info(f"Added songs: {added_songs}")
        Twitter.changes_playlist_tweet(get_song_list_from_id(added_songs), "add_announcements.json")

    if removed_songs:
        logger.info(f"Removed songs: {removed_songs}")
        Twitter.changes_playlist_tweet(get_song_list_from_id(removed_songs), "remove_announcements.json")

    db.remove_songs(removed_songs)
    db.add_songs(playlist_api_result)
    db.add_playlist_snapshot(current_snapshot)


if __name__ == "__main__":
    pass
