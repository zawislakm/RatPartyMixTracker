import os

import mysql.connector
from statistics import mean
import random
from dotenv import load_dotenv

load_dotenv()
DATABASE_HOST: str = os.getenv("DATABASE_HOST")
DATABASE_USER: str = os.getenv("DATABASE_USER")
DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME: str = os.getenv("DATABASE_NAME")


class DatabaseConnection:
    db_cursor = None
    mydb = None
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.mydb = mysql.connector.connect(
                host=DATABASE_HOST,
                user=DATABASE_USER,
                passwd=DATABASE_PASSWORD,
                database=DATABASE_NAME
            )

            cls.db_cursor = cls.mydb.cursor()
            return cls.__instance
        else:
            return cls.__instance

    @classmethod
    def close_connection(cls):
        if cls.__instance is not None:
            cls.db_cursor.close()
            cls.mydb.commit()
            cls.mydb.close()

        cls.__instance = None


# Variables
SHUFFLE_RANGE = 10
AVERAGE_LOWER = 3


def get_daily_song_database() -> str:
    global SHUFFLE_RANGE, AVERAGE_LOWER
    db: DatabaseConnection = DatabaseConnection()

    sql: str = "SELECT song_id,counter FROM daily_song_counter"
    db.db_cursor.execute(sql)

    songs: list = db.db_cursor.fetchall()

    average_daily_appearance = mean(map(lambda x: x[1], songs))
    print(average_daily_appearance)

    while True:
        for _ in range(random.randint(0, SHUFFLE_RANGE)):
            random.shuffle(songs)
        song_id, daily_appearance = random.choice(songs)

        if daily_appearance < average_daily_appearance + AVERAGE_LOWER:
            break

    sql: str = "SELECT spotify_id FROM songs WHERE song_id = %s"
    db.db_cursor.execute(sql, (song_id,))
    daily_song_spotify_id: str = db.db_cursor.fetchall()[0][0]

    sql: str = "UPDATE daily_song_counter SET counter = counter + 1 WHERE song_id = %s"
    db.db_cursor.execute(sql, (song_id,))

    print(song_id, daily_song_spotify_id)
    return daily_song_spotify_id


def get_song_spotify_ids_database() -> set:
    db: DatabaseConnection = DatabaseConnection()

    sql: str = "SELECT spotify_id FROM songs"
    db.db_cursor.execute(sql)
    songs_ids: set = set(map(lambda x: x[0], db.db_cursor.fetchall()))

    return songs_ids


def remove_songs_database(removed_song: set) -> None:
    db: DatabaseConnection = DatabaseConnection()

    for spotify_id in removed_song:
        sql: str = "DELETE FROM songs WHERE spotify_id = %s"
        db.db_cursor.execute(sql, (spotify_id,))


def update_songs_database(playlist: list) -> None:
    db: DatabaseConnection = DatabaseConnection()

    for song in playlist:
        sql: str = (
            "INSERT INTO songs (spotify_id,song_name,added_by,added_at) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE "
            "spotify_id = %s")
        db.db_cursor.execute(sql, (song.spotify_id, song.song_name, song.added_by, song.added_at, song.spotify_id))

        sql: str = "SELECT song_id FROM songs WHERE spotify_id = %s "
        db.db_cursor.execute(sql, (song.spotify_id,))
        database_song_id = db.db_cursor.fetchall()[0][0]

        for artist in song.artists_list:
            sql: str = "INSERT INTO artists (spotify_id,artist_name) VALUES (%s,%s) ON DUPLICATE KEY UPDATE spotify_id = %s"
            db.db_cursor.execute(sql, (artist.spotify_id, artist.artist_name, artist.spotify_id))

            sql: str = "SELECT artist_id FROM artists WHERE spotify_id = %s "
            db.db_cursor.execute(sql, (artist.spotify_id,))
            database_artist_id = db.db_cursor.fetchall()[0][0]

            sql: str = (
                "INSERT INTO songs_by_artists (artist_id,song_id) VALUES (%s,%s) ON DUPLICATE KEY UPDATE song_id = %s , "
                "artist_id = %s")
            db.db_cursor.execute(sql, (database_artist_id, database_song_id, database_song_id, database_artist_id))


if __name__ == "__main__":
    pass
