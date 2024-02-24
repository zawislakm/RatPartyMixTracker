from datetime import datetime, date

from fastapi import Depends, APIRouter, Request, HTTPException
from pydantic import BaseModel

import src.API.auth as auth
from src.Database import Database as db
from src.Database.models import Song

dailysong_router = APIRouter(prefix="/dailysong", tags=["dailysong"])


class DailySongSetRequest(BaseModel):
    spotify_id: str
    date: str


@dailysong_router.post("/set")
async def set_daily_song(request: Request, verify: bool = Depends(auth.check_token)) -> dict:
    song_data = await request.json()

    try:
        daily_song_request = DailySongSetRequest(**song_data)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid request body")

    song_date = datetime.fromisoformat(daily_song_request.date).date()

    if song_date <= date.today():
        raise HTTPException(status_code=400, detail="Forbidden to set song for past days and current day")

    try:
        db.set_daily_song(spotify_id=daily_song_request.spotify_id, song_date=song_date)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "Song successfully set for the specified date", "success": True}


@dailysong_router.get("/get")
async def get_daily_song(verify: bool = Depends(auth.check_token)) -> Song:
    return db.get_daily_song()


if __name__ == "__main__":
    pass
