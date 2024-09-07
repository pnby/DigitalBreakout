import os

from dotenv import load_dotenv
from envparse import env

load_dotenv()

BOT_TOKEN = env.str("BOT_TOKEN")
MONGO_URI = os.environ.get('MONGO_URI', "mongodb://localhost:27017/prod")
