from info import DATABASE_URI

# Bot information
SESSION = 'Media_search'
USER_SESSION = 'Wednesday_v2_bot'
API_ID = '13357171'
API_HASH = 'd39c4324a40a8a6b27a067f8ff2b987e'
BOT_TOKEN = '7174411060:AAEQCnvh__ks7II0UpoLEj8jGyL3mOd4L0U'
USERBOT_STRING_SESSION = ''

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = '6976445947'
CHANNELS = '-1001871354889'
AUTH_USERS = []
AUTH_CHANNEL = '-1001668695643'

# MongoDB information
DATABASE_NAME = 'cluster0'
COLLECTION_NAME = 'mongodb+srv://akagameres:akagrameres@cluster0.xtcxn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'  # If you are using the same database, then use different collection name for each bot

#temp dict for storing the db uri which will be used for storing user, chat and file infos
tempDict = {'mongodb+srv://akagameres:akagrameres@cluster0.xtcxn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0': DATABASE_URI}
