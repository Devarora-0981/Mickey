import os
from pyrogram.types import *
from config import *


DEV_OP = [
    [
        InlineKeyboardButton(text="🥀 ᴏᴡɴᴇʀ 🥀", url=f"tg://settings"),
        InlineKeyboardButton(text="✨ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/{TheLove2Forever}"),
    ],
    [
        InlineKeyboardButton(
            text="🧸 ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ 🧸",
            url=f"https://t.me/{Evaa_Chatt_Bot}?startgroup=true",
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
             url=f"https://t.me/{Evaa_Chatt_Bot}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="✨ ᴄʟᴏsᴇ ✨", 
                              callback_data="PCLOSE",
         ),
     ],
]


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


S_BACK = [
   [ 
       InlineKeyboardButton(text="🐳 ʙᴀᴄᴋ 🐳", callback_data="SBACK"),
       InlineKeyboardButton(text="🌲 ᴄʟᴏsᴇ 🌲", callback_data="CLOSE"),
   ],
]


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
           InlineKeyboardButton(text="🚀 ʜᴇʟᴘ 🚀", url=f"https://t.me/{Evaa_Chatt_Bot}?start=help"),
           InlineKeyboardButton(text="🐳 ᴄʟᴏsᴇ 🐳", callback_data="CLOSE"),
     ],
]


ABOUT_BTN = [
      [
           InlineKeyboardButton(text="🎄 sᴜᴘᴘᴏʀᴛ 🎄", url=f"https://t.me/{TheLove2Forever}"),  
           InlineKeyboardButton(text="🚀 ʜᴇʟᴘ 🚀", callback_data="HELP"),
      ],
      [    
           InlineKeyboardButton(text="🍾 ᴏᴡɴᴇʀ 🍾", url=f"https://t.me/{ii_Romana_ii}"), 
           InlineKeyboardButton(text="❄️ sᴏᴜʀᴄᴇ ❄️", callback_data="SOURCE"),
      ],
      [ 
           InlineKeyboardButton(text="🐳 ᴜᴘᴅᴀᴛᴇs 🐳", url=f"https://t.me/{TheLove2Forever}"),  
           InlineKeyboardButton(text="✨ ʙᴀᴄᴋ ✨", callback_data="BACK"),
      ],
]









