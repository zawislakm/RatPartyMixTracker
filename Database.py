import os
import random
from collections import Counter
from datetime import date

from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine, select

from models import Song, DailySong, Artist, SongsByArtists

load_dotenv()
DATABASE_HOST: str = os.getenv("DATABASE_HOST")
DATABASE_USER: str = os.getenv("DATABASE_USER")
DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME: str = os.getenv("DATABASE_NAME")

DATABASE_URL = f'mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'

ENGINE = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(ENGINE)

# Variables
SHUFFLE_RANGE: int = 10
AVERAGE_LOWER: int = 3


def select_songs() -> list:
    with Session(ENGINE) as session:
        statement = select(Song)
        results = session.exec(statement)
        songs = list(results.all())

        return songs


def select_song_by_song_id(song_id: int) -> Song:
    with Session(ENGINE) as session:
        statement = select(Song).where(Song.song_id == song_id)
        result = session.exec(statement)
        song = result.one()

        return song


def get_songs_spotify_ids() -> set:
    return set(map(lambda x: x.spotify_id, select_songs()))


def get_songs_song_ids() -> set:
    return set(map(lambda x: x.song_id, select_songs()))


def get_random_song_id() -> int:
    global SHUFFLE_RANGE
    songs_ids = list(get_songs_song_ids())

    for _ in range(SHUFFLE_RANGE):
        random.shuffle(songs_ids)

    return random.choice(songs_ids)


def select_artists() -> list:
    with Session(ENGINE) as session:
        statement = select(Artist)
        results = session.exec(statement)
        artists = list(results.all())

        return artists


def get_artists_spotify_ids() -> set:
    return set(map(lambda x: x.spotify_id, select_artists()))


def remove_songs(removed_songs: set) -> None:
    with Session(ENGINE) as session:
        for song_spotify_id in removed_songs:
            statement = select(Song).where(Song.spotify_id == song_spotify_id)
            result = session.exec(statement)
            removed_song = result.one()
            session.delete(removed_song)
            session.commit()


def insert_element(obj: Song | Artist) -> int:
    with Session(ENGINE) as session:
        model_type = type(obj).__name__
        existing_obj = session.exec(
            select(obj.__class__).where(getattr(obj.__class__, "spotify_id") == getattr(obj, "spotify_id"))).first()

        if existing_obj is not None:
            existing_obj.update(obj)
            session.add(existing_obj)
            session.commit()
            obj = existing_obj
        else:
            session.add(obj)
            session.commit()
            session.refresh(obj)

        return getattr(obj, f"{model_type.lower()}_id")


def add_songs(playlist: list) -> None:
    with Session(ENGINE) as session:
        for song in playlist:
            song_id = insert_element(song)

            for artist in song.get_artists():
                artist_id = insert_element(artist)

                songs_by_artist = SongsByArtists(song_id=song_id, artist_id=artist_id)
                statement = select(SongsByArtists).where(
                    (SongsByArtists.song_id == song_id and SongsByArtists.artist_id == artist_id))
                relation = session.exec(statement).first()
                if relation is None:
                    session.add(songs_by_artist)
                    session.commit()


def get_daily_song() -> Song:
    with Session(ENGINE) as session:
        daily_song = None

        statement = select(DailySong).where(DailySong.song_date == date.today())
        result = session.exec(statement).first()

        if result is not None:
            # get daily song
            daily_song = select_song_by_song_id(result.song_id)
        else:
            # set daily song
            daily_song = set_daily_song()

        return daily_song


def set_daily_song() -> Song:
    global AVERAGE_LOWER, SHUFFLE_RANGE

    with Session(ENGINE) as session:
        statement = select(DailySong)
        result = session.exec(statement)
        daily_songs_counter = Counter(song.song_id for song in result.all())

        songs_ids = list(get_songs_song_ids())
        avg_daily_appearance = sum(daily_songs_counter.values()) / len(songs_ids)

        while True:

            for _ in range(SHUFFLE_RANGE):
                random.shuffle(songs_ids)

            song_id = random.choice(songs_ids)

            if daily_songs_counter.get(song_id, 0) < avg_daily_appearance + AVERAGE_LOWER:
                break

        daily_song = DailySong(song_date=date.today(), song_id=song_id)

        session.add(daily_song)
        session.commit()

        return select_song_by_song_id(song_id)


if __name__ == "__main__":
    pass
    get_daily_song()
