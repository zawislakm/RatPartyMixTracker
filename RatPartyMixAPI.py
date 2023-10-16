from fastapi import FastAPI
import json
from Database import get_daily_song_database

app = FastAPI()

@app.get("/ratpartymix/dailysong")
async def home_page():
    data_set = {'SpotifyID': get_daily_song_database()}
    return data_set

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8443)
