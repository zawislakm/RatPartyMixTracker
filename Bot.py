import Database as db
import Spotify
import Twitter


def get_song_list_from_id(songs: set) -> list:
    return list(map(lambda x: Spotify.get_song_by_id(x), songs))


def check_update() -> None:
    playlist_api_result = Spotify.get_playlist_elements()

    if not playlist_api_result:  # no updates on playlist :(
        return

    old_songs = db.get_songs_spotify_ids()

    new_songs = set(map(lambda x: x.spotify_id, playlist_api_result))

    added_songs = new_songs - old_songs
    removed_songs = old_songs - new_songs

    if added_songs:
        print(f"Added songs: {added_songs}")
        Twitter.changes_playlist_tweet(get_song_list_from_id(added_songs), "add_announcements.json")

    if removed_songs:
        print(f"Removed songs: {removed_songs}")
        Twitter.changes_playlist_tweet(get_song_list_from_id(removed_songs), "remove_announcements.json")

    db.remove_songs(removed_songs)
    db.add_songs(playlist_api_result)


if __name__ == "__main__":
    check_update()
