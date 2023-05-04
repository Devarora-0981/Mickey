# Don't remove This Line From Here. Tg: @Dev_Arora_0981 | @DevArora0981
# Github :- Devarora-0981 | Devarora2604
import random
from datetime import datetime

from inline import *
from pyrogram import filters
from pyrogram.types import *
from read import *

from config import OWNER_USERNAME
from Mickey import App
from Mickey.database import *
from Mickey.modules.helpers import *


@App.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(client: App, message: Message):
    if message.chat.type == "private":
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
    await message.delete()
    start = datetime.now()
    wtfbhemchomd = await message.reply_sticker(sticker=random.choice(STICKER))
    ms = (datetime.now() - start).microseconds / 1000
    me = await client.get_me()
    await message.reply_photo(
        photo=random.choice(PHOTO),
        caption=f"нey вαву!!\n**[{me.first_name}](t.me/{me.username})** ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n➥ `{ms}` ms\n\n<b>||мαdє ωιтн ❣️ ву [ᴅᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/{OWNER_USERNAME})||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
