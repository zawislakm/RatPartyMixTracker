import Spotify
import Twitter


if __name__ == "__main__":
    removed, added = Spotify.work_script()

    if len(removed) != 0:
        print(len(removed))
        Twitter.removed_songs_tweet(removed)

    if len(added) != 0:
        Twitter.added_songs_tweet(added)
