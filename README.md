# Playlist tracking app

A code that tracks real-time changes to a playlist on Spotify.
It provides updates about playlist changes and selects a daily song for Twitter followers every day.

## Technology core

- Python 3.10 with [SQLModel, FastAPI, Tweepy and others](https://github.com/zawislakm/RatPartyMixTracker/blob/master/config_files/requirements.txt)
- MySQL
- Oracle Cloud - VM
- Linux

The application is hosted on Oracle Cloud using a Virtual Machine (Ubuntu 20.04).
A MySQL database is used for storing playlist information. API provides information about daily song to 
[DiscordBot]((https://github.com/JakubDralus/discord-bot)) and allows to set a new daily songs for upcoming days.
To ensure the continuous operation of the API, monitoring playlist changes, and daily song post to Twitter,
respective commands have been added to the OS in the /etc/systemd/system/ directory.

![database schema](https://github.com/zawislakm/RatPartyMixTracker/blob/master/config_files/database_schema.png)


## RatPartMix links

1. [RatPartMix - Spotify](https://open.spotify.com/playlist/0RHhiQ6hGLKgjE7eqNdXzh?si=42gbm0djRZ25L4x0Tq-d_Q&nd=1)
2. [RatPartyMix - Twitter](https://twitter.com/RatPartyMix)
3. [RatPartMix - DiscordBot](https://github.com/JakubDralus/discord-bot)
4. [RatPartyMix - API](http://130.61.63.141:8888/docs)




