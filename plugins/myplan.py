import time
from datetime import datetime, date
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.database import find_one, used_limit, daily, uploadlimit, usertype
from helper.date import check_expi
from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["myplan"]))
async def myplan(client, message):
    user_data = find_one(message.from_user.id)
    limit = user_data.get("uploadlimit", 0)
    used = user_data.get("used_limit", 0)
    user_type = user_data.get("usertype", "Free")
    pre_expiration = user_data.get("prexdate")

    if pre_expiration and not check_expi(pre_expiration):
        uploadlimit(message.from_user.id, 16384000000)
        usertype(message.from_user.id, "Free")

    if not pre_expiration or not check_expi(pre_expiration):
        today = int(time.mktime(date.today().timetuple()))
        daily(message.from_user.id, today)
        used_limit(message.from_user.id, 0)

    remain = limit - used
    normal_date = None
    if pre_expiration:
        normal_date = datetime.fromtimestamp(pre_expiration).strftime('%Y-%m-%d')

    text = f"ᴜꜱᴇʀ ɪᴅ:- `{message.from_user.id}`\nᴘʟᴀɴ :- {user_type}\nᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ :- {humanbytes(limit)}\nᴛᴏᴅᴀʏ ᴜꜱᴇᴅ :- {humanbytes(used)}\nʀᴇᴍᴀɪɴ:- {humanbytes(remain)}"
    if normal_date:
        text += f"\n\nʏᴏᴜʀ ᴘʟᴀɴ ᴇɴᴅꜱ ᴏɴ :- {normal_date}"

    reply_markup = None
    if user_type == "Free":
        reply_markup = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("💳 ᴜᴘɢʀᴀᴅᴇ", callback_data="upgrade"),
            ],
            [
                InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ ✖️", callback_data="cancel")
            ]
        ])
    await message.reply(text, quote=True, reply_markup=reply_markup)

