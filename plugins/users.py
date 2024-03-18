import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import *
from helper.database import botdata, find_one, total_user, getid
from helper.progress import humanbytes


# Define command handler
@Client.on_message(filters.private & filters.user(ADMINS) & filters.command(["users"]))
async def users(client, message):
    botdata(int(BOT_TOKEN.split(':')[0]))
    data = find_one(int(BOT_TOKEN.split(':')[0]))
    total_rename = data["total_rename"]
    total_size = data["total_size"]
    id = str(getid())
    ids = id.split(',')

    ids_list = "\n".join([f"{index}. {user_id}" for index, user_id in enumerate(ids, start=1)])

    await message.reply_text(
        f"🛗 ᴛᴏᴛᴀʟ ᴜꜱᴇʀ :- {total_user()}\n\n"
        f"📂 ᴛᴏᴛᴀʟ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ :- {total_rename}\n"
        f"🗃️ ᴛᴏᴛᴀʟ ꜱɪᴢᴇ ʀᴇɴᴀᴍᴇᴅ :- {humanbytes(int(total_size))}\n\n"
        f"🆔 ᴀʟʟ ɪᴅꜱ :\n{ids_list}",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✖️ ᴄʟᴏꜱᴇ ✖️", callback_data="cancel")
                ]
            ]
        )
    )
