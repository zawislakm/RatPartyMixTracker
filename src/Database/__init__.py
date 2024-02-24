import os

from dotenv import load_dotenv

load_dotenv()
DATABASE_HOST: str = os.getenv("DATABASE_HOST")
DATABASE_USER: str = os.getenv("DATABASE_USER")
DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME: str = os.getenv("DATABASE_NAME")
