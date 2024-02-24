import os

from dotenv import load_dotenv

load_dotenv()
CLIENT_ID: str = os.getenv("CLIENT_ID")
CLIENT_SECRET: str = os.getenv("CLIENT_SECRET")
RAT_PARTY_MIX_ID: str = os.getenv("RAT_PARTY_MIX_ID")


API_KEY_TWITTER: str = os.getenv('API_KEY_TWITTER')
API_KEY_SECRET_TWITTER: str = os.getenv('API_KEY_SECRET_TWITTER')
BEARER_TOKEN_TWITTER: str = os.getenv('BEARER_TOKEN_TWITTER')
ACCESS_TOKEN_TWITTER: str = os.getenv('ACCESS_TOKEN_TWITTER')
ACCESS_TOKEN_SECRET_TWITTER: str = os.getenv('ACCESS_TOKEN_SECRET_TWITTER')
