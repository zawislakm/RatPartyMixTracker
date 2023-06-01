import Spotify
import Twitter
from time import sleep

if __name__ == "__main__":

        removed, added = Spotify.work_script()


        if len(removed) != 0:
            Twitter.removed_songs_tweet(removed)

        if len(added) != 0:
            Twitter.added_songs_tweet(added)





