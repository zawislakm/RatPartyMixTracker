import uvicorn
from fastapi import FastAPI

import Database as db
from models import Song

app = FastAPI()


# 130.61.63.141:8443/ratpartymix/dailysong


@app.get("/ratpartymix")
async def get_homepage() -> str:
    return "Best playlist for parties, updating frequently to keep you up to date with best hits 😎"


@app.get("/ratpartymix/dailysong")
async def get_daily_song() -> Song:
    return db.get_daily_song()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8443)
