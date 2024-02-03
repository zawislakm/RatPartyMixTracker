from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

from pydantic import PrivateAttr
from sqlmodel import Field, SQLModel


@dataclass
class Artist(SQLModel, table=True):
    __tablename__ = "artists"

    spotify_id: str
    artist_name: str
    artist_id: Optional[int] = Field(default=None, primary_key=True)

    def __init__(self, data: dict) -> None:
        super().__init__()
        self.spotify_id = data["id"]
        self.artist_name = data["name"]

    def update(self, other_artist) -> None:
        self.artist_name = other_artist.artist_name


@dataclass
class Song(SQLModel, table=True):
    __tablename__ = "songs"

    song_name: str
    spotify_id: str = Field(unique=True)
    added_by: Optional[str] = Field(default=None)
    added_at: Optional[datetime] = Field(default=None)
    song_id: Optional[int] = Field(default=None, primary_key=True)

    # not in database
    _song_link: Optional[str] = PrivateAttr(default=None)
    _song_photo_link: Optional[str] = PrivateAttr(default=None)
    _popularity: Optional[int] = PrivateAttr(default=None)
    _preview_url: Optional[str] = PrivateAttr(default=None)
    _artists: Optional[list] = PrivateAttr(default_factory=list)

    def __init__(self, data: dict, added_by: str = None, added_at: str = None) -> None:
        super().__init__()
        self.song_name: str = data['name']
        self.spotify_id: str = data['id']
        self._song_link: str = data['external_urls']['spotify']
        self._song_photo_link: str = data['album']['images'][0]['url']
        self._popularity: int = data['popularity']
        self._preview_url: str = data['preview_url']

        if added_by is not None:
            self.added_by: str = added_by['id']
        if added_at is not None:
            added_at = added_at.replace("T", " ").replace("Z", "")
            self.added_at = datetime.strptime(added_at, "%Y-%m-%d %H:%M:%S")

    def update(self, other_song) -> None:
        self.song_name = other_song.song_name
        self.added_by = other_song.added_by
        self.added_at = other_song.added_at

    def add_artist(self, artist: Artist) -> None:
        self._artists.append(artist)

    def get_artists(self) -> list:
        return self._artists

    def __hash__(self) -> int:
        return hash(self.spotify_id)

    @property
    def song_link(self):
        return self._song_link

    @property
    def song_photo_link(self):
        return self._song_photo_link

    @property
    def popularity(self) -> int:
        return self._popularity


@dataclass
class SongsByArtists(SQLModel, table=True):
    __tablename__ = "songs_by_artists"

    artist_id: Optional[int] = Field(default=None, foreign_key="artists.artist_id", primary_key=True)
    song_id: Optional[int] = Field(default=None, foreign_key="songs.song_id", primary_key=True)


@dataclass
class DailySong(SQLModel, table=True):
    __tablename__ = "daily_song"

    song_date: date = Field(unique_items=True)
    song_id: Optional[int] = Field(default=None, foreign_key="songs.song_id", primary_key=True)
