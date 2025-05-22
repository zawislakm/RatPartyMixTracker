import random
from collections import Counter
from datetime import date

from sqlmodel import Session, SQLModel, select
from sqlmodel import create_engine

from src.Database.__init__ import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME
from src.Database.models import Song, DailySong, Artist, SongsByArtists, PlaylistSnapshot

DATABASE_URL = f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432/{DATABASE_NAME}'

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
        # select * from songs where song_id = song_id SQL
        result = session.exec(statement)
        song = result.first()

        if song is None:
            raise ValueError("Song with given song_id does not exist in database")

        return song


def select_song_by_spotify_id(spotify_id: str) -> Song:
    with Session(ENGINE) as session:
        statement = select(Song).where(Song.spotify_id == spotify_id)
        result = session.exec(statement)
        song = result.first()

        if song is None:
            raise LookupError("Song with given spotify_id does not exist in database")

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


def insert_element(obj) -> int:  # Song | Artist
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
    daily_song = select_daily_song_by_date(date.today())
    if daily_song is None:
        daily_song = pick_daily_song()

    return daily_song


def select_daily_song_by_date(song_date: date) -> Song | None:
    with Session(ENGINE) as session:
        statement = select(DailySong).where(DailySong.song_date == song_date)
        result = session.exec(statement).first()
        if result is None:
            return None
        daily_song = select_song_by_song_id(result.song_id)
        return daily_song


def set_daily_song(song_date: date, song_id: int = None, spotify_id: str = None) -> None:
    if song_date < date.today():
        raise ValueError("You cannot set song for past days")

    if select_daily_song_by_date(song_date) is not None:
        raise ValueError("Daily song for given date is already set")

    if spotify_id is not None:
        song = select_song_by_spotify_id(spotify_id)
        song_id = song.song_id

    with Session(ENGINE) as session:
        daily_song = DailySong(song_date=song_date, song_id=song_id)
        session.add(daily_song)
        session.commit()


def pick_daily_song() -> Song:
    global AVERAGE_LOWER, SHUFFLE_RANGE

    with Session(ENGINE) as session:
        statement = select(DailySong)
        result = session.exec(statement)
        daily_songs_counter = Counter(song.song_id for song in result.all())

        songs_ids = list(get_songs_song_ids())
        try:
            avg_daily_appearance = sum(daily_songs_counter.values()) / len(songs_ids)
        except ZeroDivisionError:
            avg_daily_appearance = 0

        while True:

            for _ in range(SHUFFLE_RANGE):
                random.shuffle(songs_ids)

            song_id = random.choice(songs_ids)

            if daily_songs_counter.get(song_id, 0) < avg_daily_appearance + AVERAGE_LOWER:
                break

        set_daily_song(song_id=song_id, song_date=date.today())

        return select_song_by_song_id(song_id)


def add_playlist_snapshot(snapshot_id: str) -> None:
    with Session(ENGINE) as session:
        snapshot = PlaylistSnapshot(snapshot_id=snapshot_id)
        session.add(snapshot)
        session.commit()


def check_if_current_snapshot_in_db(current_snapshot_id: str) -> bool:
    with Session(ENGINE) as session:
        statement = select(PlaylistSnapshot).where(PlaylistSnapshot.snapshot_id == current_snapshot_id)
        result = session.exec(statement)
        snapshot = result.first()
        return snapshot is not None


if __name__ == "__main__":
    pass
