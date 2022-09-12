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

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
MONGO_URL = os.environ.get("MONGO_URL", None)
GET_ME = os.environ.get("GET_ME", None) 


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
    "https://telegra.ph/file/3abb496a639e4911be956.jpg",
    "https://telegra.ph/file/bf6a3b64608eff21a9f74.jpg",
    "https://telegra.ph/file/50ee047a8725d2bfc6e95.jpg",
    "https://telegra.ph/file/47f1f43fc3f270d64ee2f.jpg",
    "https://telegra.ph/file/fa84c7ef0e928559306db.png",
    "https://telegra.ph/file/72b6383dec320606c324d.png",
    "https://telegra.ph/file/41114c423770f85a9999a.jpg",
    "https://telegra.ph/file/2100ba0c540895c02b677.png",
    "https://telegra.ph/file/52e30d9bab966f5a3b434.png",
    "https://telegra.ph/file/c5a535e0431604b3e2d7d.png",
    "https://telegra.ph/file/52a3e2d489fd2f08eb8b9.png",
    "https://telegra.ph/file/99feee933000e8a497ddf.png",
    "https://telegra.ph/file/17ab4c1b7a5c56f815885.png",
]

EMOJIOS = [ 
      "💣",
      "💥",
      "🪄",
      "🧨",
      "⚡",
      "❄️",
      "🤡",
      "👻",
      "🎃",
      "🎩",
      "🕊",
      "🕷️",
]
      
STICKER = [
      "CAACAgUAAxkBAAJGIGMJFt2-r9xOLr7lL1L7am-q5jBJAAIcAwACRkjxVjVvKkhzlK7LKQQ",
      "CAACAgUAAxkBAAJGI2MJFvltQN6C2jCVL3ODVMUDLu5wAALSAgAC2QQpV9rletyODm9RKQQ",
      "CAACAgUAAxkBAAJGJmMJFxKEtpzp5haXbeuMclH9lThYAALzAgACkxExVofbsFCERvUMKQQ",
      "CAACAgUAAxkBAAJGKWMJFytS1z_SGyVirU0nSj3mQg3SAAKtAgACEdswVkC0WB_0uHeqKQQ",
      "CAACAgUAAxkBAAJGLGMJF0Pup2oX6wz5S1m-FLoS6DkQAAIZAwACZiEwVjcy4kxNywZcKQQ",
      "CAACAgUAAxkBAAJGL2MJF1x2q6QWheiNhNetHDWAaDp4AAJfAgACbOY5VtusF7q1pF61KQQ",
      "CAACAgUAAxkBAAJGSWMJGPFgN4bdXXhEdHcGObsm7LYdAALzAgACkxExVofbsFCERvUMKQQ",
      "CAACAgUAAxkBAAJGOWMJF-9bNEnqk8DPhMpXXWnWcTfMAAKAAgACO9LBVwTgfA-O-iEVKQQ",
      "CAACAgUAAxkBAAItc2MM7J1bWHIKubGyaT_udoFNN3oNAAICAgAClr1BV-C7cOD8Rrd5KQQ",
      "CAACAgUAAxkBAAItcmMM7J06A05BzFni6_u4eNH_ii69AAL-BAAC6wFBV1XSXHLHEFQ-KQQ",
      "CAACAgUAAxkBAAItcWMM7J1whtCHde9R80D85QpdVz9TAAKmAQACCLBAVwF80M4P2Vh4KQQ",
      "CAACAgUAAxkBAAItcGMM7J3Bswo-TALmzRZzC7rgWGNoAAKUAgAChzhAV2spD_QEnotmKQQ",
      "CAACAgUAAxkBAAItb2MM7J2GN5wJSuBEiWo7oGxd0SmOAAIBAgACwqRAVyMW6dYJ-_xSKQQ",
      "CAACAgUAAxkDAAItdmMM7M9481z7RBw6fFPxlLOR7HQ8AAIICAACruVoVNbi3F6HQlOEKQQ",
]

DEV_OP = [
    [
        InlineKeyboardButton(text="🥀 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🥀", url=f"https://t.me/Dev_arora_0981"),
        InlineKeyboardButton(text="✨ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/we_rfriends"),
    ],
    [
        InlineKeyboardButton(
            text=" ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ",
            url=f"https://t.me/spodormon_bot?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="❄️ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ❄️", url=f"https://github.com/Devarora0981/Demv-Vimk"),
        InlineKeyboardButton(text="☁️ ᴜᴘᴅᴀᴛᴇs ☁️", url=f"https://t.me/devbotz"),
    ],
]

@bot.on_message(filters.command(["start", "aistart"]))
async def restart(client, m: Message):
    accha = await m.reply_text(
                text = random.choice(EMOJIOS),
    )
    await asyncio.sleep(1.65)
    await accha.edit("**ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ sᴛᴀʀᴛɪɴɢ..**")
    await asyncio.sleep(0.75)
    await accha.edit("**ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ sᴛᴀʀᴛɪɴɢ.....**")
    await asyncio.sleep(0.75)
    await accha.edit("**ᴘʀᴇᴘᴀʀɪɴɢ ᴀ ʙᴇᴀᴜᴛɪғᴜʟ sᴛᴀʀᴛ!!**")
    await asyncio.sleep(1.25)
    await accha.edit("**ʟᴇᴛ's ɢᴏ ... 1**") 
    await asyncio.sleep(0.75)
    await accha.edit("**ʟᴇᴛ's ɢᴏ ... 2**")
    await asyncio.sleep(0.75)
    await accha.edit("**ʟᴇᴛ's ɢᴏ ... 3**")
    await asyncio.sleep(0.75)
    await accha.edit("**ᴀɴᴅ ғɪɴᴀʟʟʏ...**")
    await asyncio.sleep(0.5)
    await accha.delete()
    umm = await m.reply_sticker(
              sticker = random.choice(STICKER),
    )
    await asyncio.sleep(3)
    await umm.delete()
    await m.reply_photo(
        photo = random.choice(PHOTO),
        caption=f"""**๏ ʜᴇʏ, ɪ ᴀᴍ [sᴘᴏᴅᴇʀᴍᴏɴ ʙᴏᴛ](t.me/Spodormon_bot)**\n**➻ ᴀɴ ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**\n**──────────────────**\n**➻ ᴜsᴀɢᴇ /chatbot [on/off]**\n**๏ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴜsᴇ /help**""",
        reply_markup=InlineKeyboardMarkup(DEV_OP),
    )
@bot.on_message(filters.command(["help", "chelp", "aihelp"]))
async def restart(client, message):
    hmm = await message.reply_text("**ᴜsᴀɢᴇ ☟︎︎︎**\n**➻ ᴜsᴇ** `/chatbot on` **ᴛᴏ ᴇɴᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ.**\n**➻ ᴜsᴇ** `/chatbot off` **ᴛᴏ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.**\n**➻ ɴᴏᴛᴇ » ʙᴏᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!!**\n\n**©️ @Dev_Arora_0981**")

@bot.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    vickdb = MongoClient(MONGO_URL)    
    vick = vickdb["VickDb"]["Vick"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "You are not admin"
            )
    is_vick = vick.find_one({"chat_id": message.chat.id})
    if not is_vick:
        vick.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"Chatbot Disabled!")
    if is_vick:
        await message.reply_text(f"ChatBot Already Disabled")
    

@bot.on_message(
    filters.command(["chatbot on", "chatbot@{GET_ME} on"] ,prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    vickdb = MongoClient(MONGO_URL)    
    vick = vickdb["VickDb"]["Vick"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_vick = vick.find_one({"chat_id": message.chat.id})
    if not is_vick:           
        await message.reply_text(f"Chatbot Already Enabled")
    if is_vick:
        vick.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"ChatBot Enabled!")
    

@bot.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**Usage:**\n/chatbot [on/off] only in group")


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
       
bot.run()
