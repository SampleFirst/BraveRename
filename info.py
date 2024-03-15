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

ADMINS = int(environ.get("ADMINS", 0))
BOT_USERNAME = environ.get("BOT_USERNAME", "")
FLOOD = 500

# Database variables 
DATABASE_NAME = environ.get("DATABASE_NAME", "")
DATABASE_URL = environ.get("DATABASE_URL", "")

# Channel and groups
CHANNEL = environ.get('CHANNEL', "")
LOG_CHANNEL = environ.get('LOG_CHANNEL', "")
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', "")
PORT = int(environ.get("PORT", "8080"))
