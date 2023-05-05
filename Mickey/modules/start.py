# Don't remove This Line From Here. Tg: @Dev_Arora_0981 | @DevArora0981
# Github :- Devarora-0981 | Devarora2604

import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import *

from config import *
from Mickey import app
from Mickey.database import *
from Mickey.modules.helpers import *


@app.on_message(filters.command(["start", "aistart"]))
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ sтαятιиg.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ sтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**๏ ʜᴇʏ, ɪ ᴀᴍ {app.name}**\n**➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**\n**──────────────**\n**➻ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ]**\n<b>||๏ ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ||</b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@app.on_message(
    filters.command(
        ["help"], prefixes=["+", ".", "/", "-", "?", "$"]
    )
)
async def help(client: app, m: Message):
    if m.chat.type == "private":
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@app.on_message(filters.command("repo"))
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@app.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
