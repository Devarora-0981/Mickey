import re
import sys
import time
import logging
import asyncio
import importlib
from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

import config
from Mickey.modules import all_modules


logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)


boot = time.time()
mongo = MongoCli(config.MONGO_DB_URI)
db = mongo.Anonymous
OWNER = config.OWNER_ID


class App(Client):
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

    async def stop(self):
        await super().stop()

