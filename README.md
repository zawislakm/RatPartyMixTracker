# Playlist tracking app

An application monitors real-time updates to Spotify playlists,
delivering notifications about changes and select daily song for Twitter followers.

## Technology

- Python 3.10 with [SQLModel, FastAPI, Tweepy and others](https://github.com/zawislakm/RatPartyMixTracker/blob/master/config_files/requirements.txt)
- MySQL
- Oracle Cloud - VM
- Docker with GitHub Actions


The application is hosted on Oracle Cloud using a Virtual Machine (Ubuntu 20.04). MySQL database is used for 
storing playlist information. The app regularly checks for updates on the playlist and selects a 
daily song to share with Twitter followers. API provides information about daily song to 
[DiscordBot]((https://github.com/JakubDralus/discord-bot)) and allows to set a daily songs for future days. 

To ensure continuous operation, Cron jobs are employed within a Docker Image. Additionally,
GitHub Actions are utilized for building and deploying to DockerHub. The server is configured with a
[webhook](https://github.com/adnanh/webhook) from DockerHub to automatically pull the latest 
image from DockerHub and restart the container accordingly.


```mermaid
erDiagram
    ARTISTS {
        int  artist_id PK
        varchar spotify_id
        varchar artist_name
    }

    SONGS {
        int  song_id PK
        varchar spotify_id
        varchar song_name
        varchar added_by
        datetime added_at  
    }

    SONGS_BY_ARTISTS {
        int artist_id FK
        int song_id FK
    }

    DAILY_SONG {
        int  song_id FK
        date song_date
    }

ARTISTS ||--o{ SONGS_BY_ARTISTS : "artist_id"
SONGS ||--o{ SONGS_BY_ARTISTS : "song_id"
SONGS ||--o{ DAILY_SONG : "song_id"


```

## RatPartMix links

1. [RatPartMix - Spotify](https://open.spotify.com/playlist/0RHhiQ6hGLKgjE7eqNdXzh?si=42gbm0djRZ25L4x0Tq-d_Q&nd=1)
2. [RatPartyMix - Twitter](https://twitter.com/RatPartyMix)
3. [RatPartMix - DiscordBot](https://github.com/JakubDralus/discord-bot)
4. [RatPartyMix - API](http://130.61.63.141:8888/docs)




