import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import *


# Import helper functions
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

    await message.reply_text(
        f"🆔 All IDS : {ids}\n\n"
        f"🛗 Total User :- {total_user()}\n\n"
        f"📂 Total Renamed File :- {total_rename}\n"
        f"🗃️ Total Size Renamed :- {humanbytes(int(total_size))}",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✖️ Close Menu ✖️", callback_data="cancel")
                ]
            ]
        )
    )

