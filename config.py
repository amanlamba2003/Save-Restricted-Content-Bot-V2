# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "15469942"))
API_HASH = getenv("API_HASH", "3891697f2878604b7736b5280d254f8c")
BOT_TOKEN = getenv("BOT_TOKEN", "7129266873:AAE-BEy3ZjMhZqJAcWbKht-KtyYSkzqVkbw")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5016235092").split()))
MONGO_DB = getenv("MONGO_DB", null)
LOG_GROUP = getenv("LOG_GROUP", "-1002496132583")
CHANNEL_ID = int(getenv("CHANNEL_ID", null))
