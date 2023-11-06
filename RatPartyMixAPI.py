from fastapi import FastAPI
from Database import get_daily_song_database
import uvicorn

app = FastAPI()


# 130.162.243.45:8443/ratpartymix/dailysong
@app.get("/ratpartymix")
async def get_home() -> str:
    return "Best playlist for parties, updating frequently to keep you up to date with best hits 😎"


@app.get("/ratpartymix/dailysong")
async def get_daily_song() -> dict:
    data_set: dict = {'SpotifyID': get_daily_song_database()}
    return data_set


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8443)
