import os
from pyrogram import Client, filters
from helper.database import botdata, find_one
from helper.progress import humanbytes
from info import BOT_TOKEN

botid = BOT_TOKEN.split(':')[0]

@Client.on_message(filters.private & filters.command("about"))
async def about(client, message):
    botdata(int(botid))
    data = find_one(int(botid))
    total_rename = data["total_rename"]
    total_size = data["total_size"]
    await message.reply_text(
        f"Name: 4GB Rename\n"
        f"Language: Python 3\n"
        f"Library: Pyrogram 2.0\n"
        f"Server: Koyeb\n"
        f"Total Renamed Files: {total_rename}\n"
        f"Total Size Renamed: {humanbytes(int(total_size))}\n\n"
    )
    
