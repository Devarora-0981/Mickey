import asyncio
import importlib
import logging
import re
import sys
import time

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pymongo import MongoClient
from pyrogram import Client

import config

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)


boot = time.time()
mongo = MongoCli(config.MONGO_URL)
db = mongo.Anonymous

vickdb = MongoClient(config.MONGO_URL)
vick = vickdb["VickDb"]["Vick"]

OWNER = config.OWNER_ID


class MickeyBot(Client):
    def __init__(self):
        super().__init__(
            name="Mickey",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            plugins=dict(root="Mickey.modules"),
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.id = get_me.id
        self.name = get_me.mention
        self.username = get_me.username

    async def stop(self):
        await super().stop()


app = MickeyBot()
