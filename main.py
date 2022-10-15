#Don't remove This Line From Here. @Dev_Arora_0981 | @DevArora0981
#Github :- Devarora0981 | Devarora0987
from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re
import asyncio
import time
from datetime import datetime

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
MONGO_URL = os.environ.get("MONGO_URL", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME") 
UPDATE_CHNL = os.environ.get("UPDATE_CHNL")
OWNER_ID = os.environ.get("OWNER_ID")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP")
BOT_NAME = os.environ.get("BOT_NAME")
START_IMG1 = os.environ.get("START_IMG1")
START_IMG2 = os.environ.get("START_IMG2", None)
START_IMG3 = os.environ.get("START_IMG3", None)
START_IMG4 = os.environ.get("START_IMG4", None)
START_IMG5 = os.environ.get("START_IMG5", None)
START_IMG6 = os.environ.get("START_IMG6", None)
START_IMG7 = os.environ.get("START_IMG7", None)
START_IMG8 = os.environ.get("START_IMG8", None)
START_IMG9 = os.environ.get("START_IMG9", None)
START_IMG10 = os.environ.get("START_IMG10", None)
STKR = os.environ.get("STKR")
STKR1 = os.environ.get("STKR1", None)
STKR2 = os.environ.get("STKR2", None)
STKR3 = os.environ.get("STKR3", None)
STKR4 = os.environ.get("STKR4", None)
STKR5 = os.environ.get("STKR5", None)
STKR6 = os.environ.get("STKR6", None)
STKR7 = os.environ.get("STKR7", None)
STKR8 = os.environ.get("STKR8", None)
STKR9 = os.environ.get("STKR9", None)

bot = Client(
    "VickBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


PHOTO = [
    START_IMG1,
    START_IMG2,
    START_IMG3,
    START_IMG4,
    START_IMG5,
    START_IMG6,
    START_IMG7,
    START_IMG8,
    START_IMG9,
    START_IMG10,
]

EMOJIOS = [ 
      "💣",
      "💥",
      "🪄",
      "🧨",
      "⚡",
      "🤡",
      "👻",
      "🎃",
      "🎩",
      "🕊",
]
      
STICKER = [
      STKR,
      STKR1,
      STKR2,
      STKR3,
      STKR4,
      STKR5,
      STKR6,
      STKR7,
      STKR8,
      STKR9,
]
START = f"""
**๏ ʜᴇʏ, ɪ ᴀᴍ [{BOT_NAME}]({START_IMG1})**
**➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ**
**──────────────**
**➻ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ]**
<b>||๏ ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ.||</b>
"""
DEV_OP = [
    [
        InlineKeyboardButton(text="🥀 ᴏᴡɴᴇʀ 🥀", url=f"tg://settings"),
        InlineKeyboardButton(text="✨ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="🧸 ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ 🧸",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="🚀 ʜᴇʟᴘ & ᴄᴍᴅs 🚀", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="❄️ sᴏᴜʀᴄᴇ ❄️", callback_data="SOURCE"),
        InlineKeyboardButton(text="☁️ ᴀʙᴏᴜᴛ ☁️", callback_data="ABOUT"),
    ],
]
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="🧸 ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ 🧸",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="✨ sᴜᴘᴘᴏʀᴛ ✨", 
                              url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]
HELP_READ = f"""
<u>**ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {BOT_NAME}**</u>
<u>**ᴀʀᴇ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ!**</u>
**ᴀʟʟ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ:/**
**──────────────**
<b>||©️ @{OWNER_USERNAME}||</b>
"""
BACK = [
     [
           InlineKeyboardButton(text="✨ ʙᴀᴄᴋ ✨", callback_data="BACK"),
     ],
]
HELP_BTN = [
     [
          InlineKeyboardButton(text="🐳 ᴄʜᴀᴛʙᴏᴛ 🐳", callback_data="CHATBOT_CMD"),
          InlineKeyboardButton(text="🎄 ᴛᴏᴏʟs 🎄", callback_data="TOOLS_DATA"),
     ],
     [
          InlineKeyboardButton(text="✨ ʙᴀᴄᴋ ✨", callback_data="BACK"),
          InlineKeyboardButton(text="❄️ ᴄʟᴏsᴇ ❄️", callback_data="CLOSE"),
     ],
]

CLOSE_BTN = [
      [
           InlineKeyboardButton(text="❄️ ᴄʟᴏsᴇ ❄️", callback_data="CLOSE"),
      ],
]

CHATBOT_ON = [
        [
            InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data=f"addchat"),
            InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data=f"rmchat"),
        ],
]
TOOLS_DATA_READ = f"""
<u>**ᴛᴏᴏʟs ғᴏʀ {BOT_NAME} ᴀʀᴇ:**</u>
**➻ ᴜsᴇ `/repo` ғᴏʀ ɢᴇᴛᴛɪɴɢ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ!**
**──────────────**
**➻ ᴜsᴇ `/ping` ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴛʜᴇ ᴘɪɴɢ ᴏғ {BOT_NAME}**
**──────────────**
<b>||©️ @{OWNER_USERNAME}||</b>
"""

CHATBOT_READ = f"""
<u>**ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {BOT_NAME}**</u>
**➻ ᴜsᴇ `/chatbot` ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.**
**๏ ɴᴏᴛᴇ ➻ ᴛʜᴇ ᴀʙᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ᴄʜᴀᴛʙᴏᴛ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!!**
**───────────────**
<b>||©️ @{OWNER_USERNAME}||</b>
"""
CHATBOT_BACK = [
        [     
              InlineKeyboardButton(text="✨ ʙᴀᴄᴋ ✨", callback_data="CHATBOT_BACK"),
              InlineKeyboardButton(text="❄️ ᴄʟᴏsᴇ ❄️", callback_data="CLOSE"),
        ],
]
HELP_START = [
     [
            InlineKeyboardButton(text="🚀 ʜᴇʟᴘ 🚀", callback_data="HELP"),
            InlineKeyboardButton(text="🐳 ᴄʟᴏsᴇ 🐳", callback_data="CLOSE"),
     ],
]

HELP_BUTN = [
     [
           InlineKeyboardButton(text="🚀 ʜᴇʟᴘ 🚀", url=f"https://t.me/{BOT_USERNAME}?start=help"),
           InlineKeyboardButton(text="🐳 ᴄʟᴏsᴇ 🐳", callback_data="CLOSE"),
     ],
]

ABOUT_BTN = [
      [
           InlineKeyboardButton(text="🎄 sᴜᴘᴘᴏʀᴛ 🎄", url=f"https://t.me/{SUPPORT_GRP}"),  
           InlineKeyboardButton(text="🚀 ʜᴇʟᴘ 🚀", callback_data="HELP"),
      ],
      [    
           InlineKeyboardButton(text="🍾 ᴏᴡɴᴇʀ 🍾", url=f"https://t.me/{OWNER_USERNAME}"), 
           InlineKeyboardButton(text="❄️ sᴏᴜʀᴄᴇ ❄️", callback_data="SOURCE"),
      ],
      [ 
           InlineKeyboardButton(text="🐳 ᴜᴘᴅᴀᴛᴇs 🐳", url=f"https://t.me/{UPDATE_CHNL}"),  
           InlineKeyboardButton(text="✨ ʙᴀᴄᴋ ✨", callback_data="BACK"),
      ],
]
SOURCE_READ = f"**ʜᴇʏ, ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.**\n**ᴘʟᴇᴀsᴇ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ & ɢɪᴠᴇ ᴛʜᴇ sᴛᴀʀ ✯**\n**──────────────────**\n**ʜᴇʀᴇ ɪs ᴛʜᴇ [sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ](https://github.com/Devarora-0981/Mickey)**\n**──────────────────**\n**ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_GRP}).\n<b>||©️ @{OWNER_USERNAME}||</b>"

ABOUT_READ = f"""
**➻ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.**
**➻ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.**
**➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.**
**➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ**
**──────────────**
**➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{BOT_NAME}](https://t.me/{BOT_USERNAME})**
"""
@bot.on_message(filters.command(["start", "aistart", f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
    if m.chat.type == "private":
        accha = await m.reply_text(
            text = random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ sтαятιиg.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ sтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
            sticker = random.choice(STICKER),
        )
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo = random.choice(PHOTO),
            caption=f"""**๏ ʜᴇʏ, ɪ ᴀᴍ [{BOT_NAME}](t.me/{BOT_USERNAME})**\n**➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**\n**──────────────**\n**➻ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ]**\n<b>||๏ ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ||</b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
    else:
        await m.reply_photo(
                      photo = random.choice(PHOTO),
                      caption = START,
                      reply_markup = InlineKeyboardMarkup(HELP_START),
   )

@bot.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    vickdb = MongoClient(MONGO_URL)
    vick = vickdb["VickDb"]["Vick"]
    if query.data == "HELP":
        await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BTN),
                      disable_web_page_preview=True,
     )
    elif query.data == "CLOSE":
            await query.message.delete()
    elif query.data == "BACK":
            await query.message.edit(
                  text = START,
                  reply_markup=InlineKeyboardMarkup(DEV_OP),
     )
    elif query.data == "SOURCE":
            await query.message.edit(
                   text = SOURCE_READ,
                   reply_markup = InlineKeyboardMarkup(BACK),
                   disable_web_page_preview = True,

     )
    elif query.data == "ABOUT":
            await query.message.edit(
                    text = ABOUT_READ,
                    reply_markup = InlineKeyboardMarkup(ABOUT_BTN),
                    disable_web_page_preview=True,
     )
    elif query.data == "ADMINS":
            await query.message.edit(
                    text = ADMIN_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BACK_BTN), 
     )
    elif query.data== "TOOLS_DATA":
            await query.message.edit(
                    text= TOOLS_DATA_READ,
                    reply_markup = InlineKeyboardMarkup(CHATBOT_BACK),
     )
    elif query.data == "BACK_HELP":
            await query.message.edit(
                    text = HELP_READ,
                    reply_markup = InlineKeyboardMarkup(HELP_BTN),
     )
    elif query.data == "CHATBOT_CMD":
            await query.message.edit(
                    text = CHATBOT_READ,
                    reply_markup = InlineKeyboardMarkup(CHATBOT_BACK), 
     )
    elif query.data == "CHATBOT_BACK":
            await query.message.edit(
                    text = HELP_READ,
                    reply_markup = InlineKeyboardMarkup(HELP_BTN), 
     )
    elif query.data == "addchat":
        if query.from_user.id not in (await is_admins(query.message.chat.id)):
            return query.answer(
                "You don't have permissions to do this baby.",
                show_alert=True,
            )
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:           
                await query.edit_message_text(f"**ᴄʜᴀᴛ-ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.**")
            if is_vick:
                vick.delete_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(f"**ᴄʜᴀᴛ-ʙᴏᴛ ᴇɴᴀʙʟᴇᴅ ʙʏ** {query.from_user.mention}.")
    elif query.data == "rmchat":
        if query.from_user.id not in (await is_admins(query.message.chat.id)):
            return query.answer(
                "**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍs ᴛᴏ ᴅᴏ ᴛʜɪs ʙᴀʙʏ!**",
                show_alert=True,
            )
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:
                vick.insert_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(f"**ᴄʜᴀᴛ-ʙᴏᴛ ᴅɪsᴀʙʟᴇᴅ ʙʏ** {query.from_user.mention}.")
            if is_vick:
                await query.edit_message_text("**ᴄʜᴀᴛ-ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.**")
                            
@bot.on_message(filters.command("repo"))
async def repo(client, message):
    await message.reply_text(
                   text= SOURCE_READ,
                   reply_markup = InlineKeyboardMarkup(BACK),
                   disable_web_page_preview = True,
      )
@bot.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def restart(client, m: Message):
    if m.chat.type == "private":
         hmm = await message.reply_photo(
                            photo = random.choice(PHOTO),
                            caption = HELP_READ,
                            reply_markup= InlineKeyboardMarkup(HELP_BTN),
        )
    else:
        await m.reply_photo(
                      photo = random.choice(PHOTO),
                      caption = "**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
                      reply_markup = InlineKeyboardMarkup(HELP_BUTN),
      )


@bot.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "__ριиgιиg...__"
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("__ριиgιиg.....__")
        await asyncio.sleep(0.25)
        await txxt.edit_text("__ριиgιиg...__")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=random.choice(PHOTO),
                             caption=f"нey вαву!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME})** ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n➥ `{ms}` ms\n\n<b>||мαdє ωιтн ❣️ ву [Ꭰev🎋](https://t.me/Dev_Arora_0981)||</b>",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )


@bot.on_message(
    filters.command(["chatbot", f"chatbot@{BOT_USERNAME}"])
    & ~filters.private)
async def chatonoff(client: Client, message: Message):
    if not message.from_user:
        return
    else:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (await is_admins(chat_id)):
            return await message.reply_text(
                "**ʏᴏᴜ ᴀʀᴇ'ɴᴛ ᴀɴ ᴀᴅᴍɪɴ.**"
            )
        else:
            await message.reply_text(
            text="» <u>**ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴩᴛɪᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ.**</u>",
            reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
        )


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")

print(f"{BOT_NAME} ɪs ᴀʟɪᴠᴇ! ɴᴏᴡ ғᴜᴄᴋ ᴏғғ! ᴀɴᴅ ɢᴏ ᴛᴏ @Wᴇ_ʀғʀɪᴇɴᴅs ʙɪᴛᴄʜ!!")      
bot.run()
