from pymongo import MongoClient

import config

vickdb = MongoClient(config.MONGO_URL)
vick = vickdb["VickDb"]["Vick"]


from .chats import *
from .users import *
