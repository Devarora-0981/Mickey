import asyncio
import importlib
import logging
import re
import sys
import time

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client

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

OWNER = config.OWNER_ID
# DEVS = config.SUDO_USERS | config.OWNER_ID


class MickeyBot(Client):
    def __init__(self):
        super().__init__(
            name="MickeyBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            plugins=dict(root="Mickey.modules"),
        )

    async def start(self):
        await super().start()

    async def stop(self):
        await super().stop()


dev = Client(
    "Dev",
    bot_token=config.BOT_TOKEN,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    # plugins=dict(root="Mickey.modules"),
)

dev.start()

BOT_ID = config.BOT_TOKEN.split(":")[0]
x = dev.get_me()
BOT_USERNAME = x.username
