# import uvloop  # Comment it out if using on windows

from Mickey import LOGGER, App

if __name__ == "__main__":
    # uvloop.install()  # Comment it out if using on windows
    LOGGER.info("Bot Started")
    App().run()
