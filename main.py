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
]

EMOJIOS = [ 
      "💣",
      "💥",
      "🪄",
      "🧨",
      "⚡",
      "⚡",
      "❄️",
      "☀️",
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
]

DEV_OP = [
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/Dev_arora_0981"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/we_rfriends"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/spodormon_bot?startgroup=true",
        ),
    ],
]

@bot.on_message(filters.command(["start", "aistart"]))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply_text(
                text = random.choice(EMOJIOS),
    )
    await asyncio.sleep(1.5)
    await accha.edit("**ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ sᴛᴀʀᴛɪɴɢ..**")
    await asyncio.sleep(0.75)
    await accha.edit("**ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ sᴛᴀʀᴛɪɴɢ.....**")
    await asyncio.sleep(0.75)
    await accha.edit("**ᴘʀᴇᴘᴀʀɪɴɢ ᴀ ʙᴇᴀᴜᴛɪғᴜʟ sᴛᴀʀᴛ!!**")
    await asyncio.sleep(1.5)
    await accha.edit("**ʟᴇᴛ's ɢᴏ ... 1**") 
    await asyncio.sleep(0.75)
    await accha.edit("**ʟᴇᴛ's ɢᴏ ... 2**")
    await asyncio.sleep(0.75)
    await accha.edit("**ʟᴇᴛ's ɢᴏ ... 3**")
    await asyncio.sleep(0.75)
    await accha.edit("**ᴀɴᴅ ғɪɴᴀʟʟʏ...**")
    await asyncio.sleep(0.5)
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(
              sticker = random.choice(STICKER),
    )
    await asyncio.sleep(3)
    await umm.delete()
    await asyncio.sleep(0.5)
    await m.reply_photo(
        photo = random.choice(PHOTO),
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ sᴘᴏᴅᴇʀᴍᴏɴ ʙᴏᴛ**\n**ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ**\n/chatbot [on/off]""",
        reply_markup=InlineKeyboardMarkup(DEV_OP),
    )

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
        await message.reply_text(f"ChatBot Is Already Disabled")
    

@bot.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
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
        await message.reply_text(f"Chatbot Is Already Enabled")
    if is_vick:
        vick.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"ChatBot Is Enable!")
    

@bot.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**Usage:**\n/chatbot [on|off] only group")


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
