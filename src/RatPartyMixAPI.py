from contextlib import asynccontextmanager

import uvicorn
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from fastapi import FastAPI, APIRouter

import src.API.auth as auth
import src.API.dailysong as dailysong
from src.jobs import check_update, post_daily_song

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth.auth_router)
api_router.include_router(dailysong.dailysong_router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_update, IntervalTrigger(minutes=30))
    scheduler.add_job(post_daily_song, CronTrigger(hour=8, minute=0))
    scheduler.start()
    try:
        yield
    finally:
        scheduler.shutdown()


app = FastAPI(lifespan=lifespan)


@api_router.get("/info", status_code=200)
async def get_info() -> str:
    return "Best playlist for parties, updating frequently to keep you up to date with best hits 😎"


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
