import os
import random
from datetime import date

import mysql.connector
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
    def close_connection(cls) -> None:
        if cls.__instance is not None:
            cls.db_cursor.close()
            cls.mydb.commit()
            cls.mydb.close()

        cls.__instance = None


# Variables
SHUFFLE_RANGE: int = 10
AVERAGE_LOWER: int = 3


def get_song_spotify_ids_database() -> set:
    db: DatabaseConnection = DatabaseConnection()

    sql: str = "SELECT spotify_id FROM songs"
    db.db_cursor.execute(sql)
    spotify_ids: set = set(map(lambda x: x[0], db.db_cursor.fetchall()))

    return spotify_ids


def get_song_ids_database() -> set:
    db: DatabaseConnection = DatabaseConnection()
    sql: str = "SELECT song_id FROM songs"
    db.db_cursor.execute(sql)
    songs_ids: set = set(map(lambda x: x[0], db.db_cursor.fetchall()))
    return songs_ids


def get_random_song_id_database() -> int:
    global SHUFFLE_RANGE
    songs_ids: list = list(get_song_ids_database())

    for _ in range(SHUFFLE_RANGE):
        random.shuffle(songs_ids)

    return random.choice(songs_ids)


def set_daily_song_database() -> int:
    global AVERAGE_LOWER
    db: DatabaseConnection = DatabaseConnection()

    sql: str = """SELECT AVG(count_ds) AS average_count
                        FROM (
                            SELECT COUNT(ds.song_id) AS count_ds
                            FROM songs
                            LEFT JOIN daily_song ds ON songs.song_id = ds.song_id
                            GROUP BY songs.song_id
                        ) AS counts;"""
    db.db_cursor.execute(sql)
    average_daily_appearance: int = db.db_cursor.fetchone()[0]

    while True:
        song_id: int = get_random_song_id_database()
        sql: str = """SELECT COALESCE(COUNT(ds.song_id), 0) AS appearance
                            FROM songs
                            LEFT JOIN daily_song ds ON songs.song_id = ds.song_id AND DATE(ds.song_date) <= CURDATE()
                            WHERE songs.song_id = %s
                            GROUP BY songs.song_id;"""
        db.db_cursor.execute(sql, (song_id,))
        song_appearance: int = db.db_cursor.fetchone()[0]

        if song_appearance < average_daily_appearance + AVERAGE_LOWER:
            break

    sql: str = "INSERT INTO daily_song (song_id, song_date) VALUES (%s, %s)"
    db.db_cursor.execute(sql, (song_id, date.today()))

    return song_id


def get_daily_song_database() -> str:
    db: DatabaseConnection = DatabaseConnection()

    sql: str = "SELECT song_id FROM daily_song WHERE song_date = %s"
    db.db_cursor.execute(sql, (date.today(),))
    result: tuple = db.db_cursor.fetchone()

    if result is None:
        song_id: int = set_daily_song_database()
    else:
        song_id: int = result[0]

    sql: str = "SELECT spotify_id FROM songs WHERE song_id = %s"
    db.db_cursor.execute(sql, (song_id,))
    spotify_id: str = db.db_cursor.fetchone()[0]
    db.close_connection()
    return spotify_id


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
        database_song_id: int = db.db_cursor.fetchall()[0][0]

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
