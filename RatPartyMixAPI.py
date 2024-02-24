import uvicorn
from fastapi import FastAPI, APIRouter, Depends

import src.API.auth as auth
import src.API.dailysong as dailysong

app = FastAPI()

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth.auth_router)
api_router.include_router(dailysong.dailysong_router)


@api_router.get("/info")
async def get_info(verify: bool = Depends(auth.check_token)) -> str:
    return "Best playlist for parties, updating frequently to keep you up to date with best hits 😎"


app.include_router(api_router)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
