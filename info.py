import re
from os import getenv, environ


id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
STRING = environ.get("STRING", "")
PICS = environ.get("PICS", "")

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "Allmoviereq_bot")
DOWNLOAD_LOCATION = "./DOWNLOADS"
FLOOD = 500

# Database variables 
DATABASE_NAME = environ.get("DATABASE_NAME", "")
DATABASE_URL = environ.get("DATABASE_URL", "")

# Channel and groups
channel = environ.get('CHANNEL')
CHANNEL = int(channel) if channel and id_pattern.search(channel) else None
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
UPDATE_CHANNEL = environ.get('UPDATE_CHANNEL', "https://t.me/iPepkornUpdate")
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', "https://t.me/iPepkornSupport")
PROMO_CHANNAL = environ.get('PROMO_CHANNEL', "https://t.me/iPepkornUpdate")
PORT = int(environ.get("PORT", "8080"))
