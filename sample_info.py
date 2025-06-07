# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'
BOT_TOKEN = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
USERBOT_STRING_SESSION = ''

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [12345789, 'admin123', 98765432]
CHANNELS = [-10012345678, -100987654321, 'channelusername']
AUTH_USERS = []
AUTH_CHANNEL = None

# MongoDB information
DATABASE_URI = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb]?retryWrites=true&w=majority"
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

DATABASE_URI_MOVIE = "mongodb://...movie"
DATABASE_NAME_MOVIE = 'MovieDB'
COLLECTION_NAME_MOVIE = 'movie_files'

DATABASE_URI_SERIES = "mongodb://...series"
DATABASE_NAME_SERIES = 'SeriesDB'
COLLECTION_NAME_SERIES = 'series_files'

# User/Admin/Referral DB
USERDATA_DB_URI = "mongodb://...userdata"
USERDATA_DB_NAME = 'UserData'
USERDATA_COLLECTION = 'users'

# Referral system
ENABLE_REFERRAL = False
REQUIRED_REFERRALS = 1

# Messages
START_MSG = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press follwing buttons and start searching.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = 'Please join @.... to use this bot'

# Channel IDs for DB mapping
MOVIE_CHANNEL_ID = -1001234567890  # Replace with your movie channel/group ID
SERIES_CHANNEL_ID = -1009876543210  # Replace with your series channel/group ID