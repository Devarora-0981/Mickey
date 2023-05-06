from Mickey import app, LOGGER

# from Mickey.modules import all_modules

"""
async def dev_boot():
    await app.start()
    for mod in await all_modules():
        importlib.import_module(f"Mickey.modules.{mod}")
    LOGGER.info("Mickey Chat Bot Started.")
    await idle()
"""


if __name__ == "__main__":
    # asyncio.get_event_loop().run_until_complete(dev_boot())
    LOGGER.info("Mickey Chat Bot Started.")
    app().run()
