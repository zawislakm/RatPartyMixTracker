from fastapi import FastAPI
from Database import get_daily_song_database

app = FastAPI()

@app.get("/ratpartymix/dailysong")
async def get_daily_song():
    data_set = {'SpotifyID': get_daily_song_database()}  # Pobieramy dane przy każdym zapytaniu
    return data_set

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8443)
