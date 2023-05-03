from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "27353035"))
API_HASH = getenv("API_HASH", "cf2a75861140ceb746c7796e07cbde9e")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID", "5350929381"))
MONGO_URL = getenv("MONGO_URL", None)
BOT_NAME = getenv("BOT_NAME")
BOT_USERNAME = getenv("BOT_USERNAME") 
SUPPORT_GRP = getenv("SUPPORT_GRP", "Nexa_Verse")
UPDATE_CHNL = getenv("UPDATE_CHNL", "DadEyeBotz")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Dev_Arora_0981")

#Random Start Images
START_IMG1 = getenv("START_IMG1")
START_IMG2 = getenv("START_IMG2")
START_IMG3 = getenv("START_IMG3")

#Random Stickers 
STKR1 = getenv("STKR1", "CAACAgQAAxkBAALRi2NZXUgjZCT775L5Nr0XrLbQ6XIpAAK_EQACpvFxHq2xh5JRVJNrKgQ")
STKR2 = getenv("STKR2", "CAACAgQAAxkBAALRjGNZXUs6YPggISBdtg4nXaU0vjNzAALqCwACbCIRU61ZQKi3F88DKgQ")
STKR3 = getenv("STKR3", "CAACAgQAAxkBAALRjWNZXUvETcfHR2Yi9ftTQLLP2uD8AAIVDAAC1SMQU-QrCHEcbz8rKgQ")
