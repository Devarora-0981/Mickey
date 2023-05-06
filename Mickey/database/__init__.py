import config
from pymongo import MongoClient

vickdb = MongoClient(config.MONGO_URL)
vick = vickdb["VickDb"]["Vick"]


from .chats import *
from .users import *
