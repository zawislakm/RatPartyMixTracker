import json
import os
from datetime import datetime, timedelta

import jwt
from dotenv import load_dotenv
from fastapi import HTTPException, Security, Request, Depends, APIRouter

auth_router = APIRouter(prefix="/auth", tags=["authentication"])

load_dotenv()
API_KEYS = json.loads(os.getenv("RAT_PARTY_MIX_API_KEYS"))
SECRET_KEY = os.getenv("RAT_PARTY_MIX_SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))


class Token:
    access_token: str
    token_type: str
    refresh_token: str

    def __init__(self, api_key: str, token_type: str = "Bearer"):
        self.access_token = self.create_access_token(api_key=api_key)
        self.token_type = token_type
        self.refresh_token = self.create_refresh_token(api_key=api_key)

    @classmethod
    def create_access_token(cls, api_key: str, expires_delta: int = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
        return jwt.encode({"id": api_key, "exp": datetime.utcnow() + timedelta(minutes=expires_delta)}, SECRET_KEY,
                          algorithm="HS256")

    @classmethod
    def create_refresh_token(cls, api_key: str, expires_delta: int = REFRESH_TOKEN_EXPIRE_DAYS) -> str:
        return jwt.encode({"id": api_key, "exp": datetime.utcnow() + timedelta(days=expires_delta)}, SECRET_KEY,
                          algorithm="HS256")

    def __str__(self) -> str:
        return self.token_type + " " + self.access_token

    def __iter__(self):
        yield "access_token", self.access_token
        yield "token_type", self.token_type
        yield "refresh_token", self.refresh_token

    def __dict__(self):
        return {
            "access_token": self.access_token,
            "token_type": self.token_type,
            "refresh_token": self.refresh_token
        }


def get_api_key(request: Request):
    try:
        api_key_request = request.headers.get("X-API-Key")  # chodzi o to w 4

        if not api_key_request:
            raise HTTPException(status_code=401, detail="Missing X-API-Key header")

        if api_key_request not in API_KEYS:
            raise HTTPException(status_code=401, detail="Invalid API Key")

        return True

    except HTTPException as exc:
        raise exc


def check_token(request: Request):
    try:
        authorization_header = request.headers.get("Authorization")
        if not authorization_header:
            raise HTTPException(status_code=401, detail="Missing Authorization header")

        _, token = authorization_header.split(" ")
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if "id" not in payload:
            raise HTTPException(status_code=400, detail="Invalid token: Missing 'id' in payload")

        return True

    except HTTPException as exc:
        raise exc
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Invalid token: Expired token")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=400, detail="Invalid token: Invalid token")


def verify_refresh_token(request: Request):
    try:
        refresh_token = request.headers.get("refresh_token")
        if not refresh_token:
            raise HTTPException(status_code=400, detail="Missing refresh_token in query parameters")

        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=["HS256"])
        if "id" not in payload:
            raise HTTPException(status_code=400, detail="Invalid token: Missing 'id' in payload")

        return True

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Invalid token: Expired refresh token")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=400, detail="Invalid token: Invalid refresh token")


@auth_router.post("/token")
async def get_access_token(request: Request, verify: bool = Security(get_api_key)) -> dict:
    token = Token(api_key=request.headers.get("X-API-Key"))
    return dict(token)


@auth_router.post("/refresh")
async def refresh_access_token(request: Request, verify: bool = Depends(verify_refresh_token)) -> dict:
    token = Token(api_key=request.headers.get("refresh_token"))
    return dict(token)
