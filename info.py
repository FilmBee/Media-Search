import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

def parse_bool(val):
    return str(val).lower() in ("true", "1", "yes")

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = parse_bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI_MOVIE = environ['DATABASE_URI_MOVIE']
DATABASE_NAME_MOVIE = environ['DATABASE_NAME_MOVIE']
COLLECTION_NAME_MOVIE = environ.get('COLLECTION_NAME_MOVIE', 'movie_files')

DATABASE_URI_SERIES = environ['DATABASE_URI_SERIES']
DATABASE_NAME_SERIES = environ['DATABASE_NAME_SERIES']
COLLECTION_NAME_SERIES = environ.get('COLLECTION_NAME_SERIES', 'series_files')

# User/Admin/Referral DB
USERDATA_DB_URI = environ['USERDATA_DB_URI']
USERDATA_DB_NAME = environ.get('USERDATA_DB_NAME', 'UserData')
USERDATA_COLLECTION = environ.get('USERDATA_COLLECTION', 'users')

# Referral system
ENABLE_REFERRAL = parse_bool(environ.get('ENABLE_REFERRAL', 'False'))
REQUIRED_REFERRALS = int(environ.get('REQUIRED_REFERRALS', 1))

# Messages
default_start_msg = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')

# Channel IDs for DB mapping
MOVIE_CHANNEL_ID = int(environ.get('MOVIE_CHANNEL_ID', '0'))  # e.g. -1001234567890
SERIES_CHANNEL_ID = int(environ.get('SERIES_CHANNEL_ID', '0'))
