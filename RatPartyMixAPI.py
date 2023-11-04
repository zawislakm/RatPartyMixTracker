from fastapi import FastAPI
from Database import get_daily_song_database
import uvicorn
app = FastAPI()

@app.get("/ratpartymix/dailysong")
async def get_daily_song():
    data_set = {'SpotifyID': get_daily_song_database()}
    return data_set

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8443)
