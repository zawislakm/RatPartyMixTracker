from datetime import datetime, date

from fastapi import Depends, APIRouter, HTTPException
from pydantic import BaseModel

import src.API.auth as auth
from src.Database import Database as db
from src.Database.models import Song

dailysong_router = APIRouter(prefix="/dailysong", tags=["dailysong"])


class DailySongSetRequest(BaseModel):
    spotify_id: str
    date: str


@dailysong_router.post("/set", status_code=201)
async def set_daily_song(daily_song_request: DailySongSetRequest, verify: bool = Depends(auth.check_token)) -> dict:
    song_date = datetime.fromisoformat(daily_song_request.date).date()

    if song_date <= date.today():
        raise HTTPException(status_code=403, detail="Forbidden to set song for past days and current day")

    try:
        db.set_daily_song(spotify_id=daily_song_request.spotify_id, song_date=song_date)
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "Song successfully set for the specified date", "success": True}


@dailysong_router.get("/get", status_code=200)
async def get_daily_song(verify: bool = Depends(auth.check_token)) -> Song:
    return db.get_daily_song()


if __name__ == "__main__":
    pass
