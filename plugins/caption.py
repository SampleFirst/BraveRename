from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import *


@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
        return await message.reply_text("**ɢɪᴠᴇ ᴍᴇ ᴀ ᴄᴀᴘᴛɪᴏɴ ᴛᴏ ꜱᴇᴛ.\n\nᴇxᴀᴍᴘʟᴇ:- `/set_caption File Name`**", quote=True)
    caption = message.text.split(" ", 1)[1]
    add_caption(int(message.chat.id), caption)
    await message.reply_text("**ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴀᴅᴅᴇᴅ ✅**", quote=True)


@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = find(int(message.chat.id))
    if not caption:
        await message.reply_text("**ʏᴏᴜ ᴅᴏɴᴛ ʜᴀᴠᴇ ᴀɴʏ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ**", quote=True)
        return
    del_caption(int(message.chat.id))
    await message.reply_text("**ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ✅**", quote=True)


@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = find(int(message.chat.id))
    if caption:
        await message.reply_text(f"<b><u>ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ:</b></u>\n\n`{caption[1]}`", quote=True)
    else:
        await message.reply_text("**ʏᴏᴜ ᴅᴏɴᴛ ʜᴀᴠᴇ ᴀɴʏ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ**", quote=True)
