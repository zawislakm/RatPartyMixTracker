import os

from dotenv import load_dotenv

load_dotenv()
API_KEYS = os.getenv("RAT_PARTY_MIX_API_KEYS")
SECRET_KEY = os.getenv("RAT_PARTY_MIX_SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))
