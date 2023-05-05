import asyncio
import importlib

from pyrogram import idle

from Mickey import app, LOGGER
from Mickey.modules import all_modules


async def dev_boot():
    try:
        await app.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)
    for mod in await all_modules():
        imported_module = importlib.import_module(f"Mickey.modules.{mod}")
    LOGGER.info("Mickey Chat Bot Started.")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(dev_boot())
    LOGGER.info("Stopping Mickey Chat Bot...")
