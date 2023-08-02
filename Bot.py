import Spotify
import Twitter
import Database


def get_song_list_from_id(song_set: set) -> list:
    song_list: list = []
    for song_id in song_set:
        song_list.append(Spotify.get_song_by_id(song_id))

    return song_list


def set_difference(first: set, second: set) -> set:
    return first - second


def check_update():
    playlist_api_result: list = Spotify.get_playlist_elements()

    if not playlist_api_result:  # no updates on playlist :(
        return

    db: Database.DatabaseConnection = Database.DatabaseConnection()
    old_songs: set = Database.get_song_spotify_ids_database()

    new_songs = set(map(lambda x: x.spotify_id, playlist_api_result))

    added_songs: set = set_difference(new_songs, old_songs)
    removed_songs: set = set_difference(old_songs, new_songs)

    if added_songs:
        print(f"Added songs: {added_songs}")
        Twitter.changes_playlist_tweet(get_song_list_from_id(added_songs), "add_announcements.json")
        # make tweet

    if removed_songs:
        print(f"Removed songs: {removed_songs}")
        Twitter.changes_playlist_tweet(get_song_list_from_id(removed_songs),"remove_announcements.json")
        # make tweet

    Database.remove_songs_database(removed_songs)
    Database.update_songs_database(playlist_api_result)

    db.close_connection()


if __name__ == "__main__":
    check_update()
