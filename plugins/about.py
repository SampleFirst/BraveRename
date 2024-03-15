import os 
from pyrogram import Client, filters
from helper.database import botdata, find_one
from helper.progress import humanbytes
from info import BOT_TOKEN

botid = BOT_TOKEN.split(':')[0]


@Client.on_message(filters.private & filters.command("about"))
async def start(client,message):
    botdata(int(botid))
    data = find_one(int(botid))
    total_rename = data["total_rename"]
    total_size = data["total_size"]
    await message.reply_text(
        f"ʙᴏᴛ ɴᴀᴍᴇ: Brave\n"
        f"ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ3\n"
        f"ʟɪʙʀᴀʀʏ: ᴘʏʀᴏɢʀᴀᴍ 2.0\n"
        f"ꜱᴇʀᴠᴇʀ: ᴋᴏʏᴇʙ\n"
        f"ᴛᴏᴛᴀʟ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ: {total_rename}\n"
        f"ᴛᴏᴛᴀʟ ꜱɪᴢᴇ ʀᴇɴᴀᴍᴇᴅ: {humanbytes(int(total_size))}\n\n"
    )

