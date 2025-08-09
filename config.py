from os import getenv
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

class Config:
    BOT_TOKEN: str = getenv("BOT_TOKEN")
    AI_TOKEN: str = getenv("AI_TOKEN")

config = Config()