import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///crypto.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BOT_TOKEN = os.getenv("BOT_TOKEN")
    PRICE_API_URL = os.getenv("PRICE_API_URL")
    UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", 300))