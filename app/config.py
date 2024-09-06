from dotenv import load_dotenv
from envparse import env

load_dotenv()

BOT_TOKEN = env.str("BOT_TOKEN")
