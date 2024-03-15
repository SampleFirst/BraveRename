from datetime import date as date_
import datetime
import os
import random
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import humanize
from helper.progress import humanbytes
from Script import script
from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
import os
from pyrogram import Client, filters, enums
import asyncio
from info import *

botid = BOT_TOKEN.split(':')[0]


currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    wish = "❤️ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ꜱᴡᴇᴇᴛʜᴇᴀʀᴛ ❤️"
    period = "AM"
elif 12 <= currentTime.hour < 16:
    wish = '🤍 ɢᴏᴏᴅ ᴀꜰᴛᴇʀɴᴏᴏɴ ᴍʏ ʟᴏᴠᴇ 🤍'
    period = "PM"
elif 16 <= currentTime.hour < 21:
    wish = '🦋 ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ ʙᴀʙʏ 🦋'
    period = "PM"
else:
    wish = '🌙 ɢᴏᴏᴅ ɴɪɢʜᴛ ᴍʏ ꜱᴡᴇᴇᴛɪᴇ 🌙'
    period = "PM"
hour_12_format = currentTime.strftime("%I:%M %p")
final_wish = f"{wish} ({hour_12_format} {period})"

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    loading_sticker_message = await message.reply_sticker("CAACAgUAAxkBAAEKDf1k3mCOA5HUO51nPYSN-yaCNFj1PQAC7QoAAgEFoFRUQkvwYhdUWTAE")
    await asyncio.sleep(2)
    await loading_sticker_message.delete()
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        txt=f"""ʜᴇʟʟᴏ {wish} {message.from_user.first_name } \n\n
➻ ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ʏᴇᴛ ᴘᴏᴡᴇʀꜰᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ. \n
➻ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ʏᴏᴜʀ ꜰɪʟᴇꜱ\n
➻ ʏᴏᴜ ᴄᴀɴ ᴀʟꜱᴏ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ ᴛᴏ ꜰɪʟᴇ ᴀɴᴅ ꜰɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ.\n 
➻ ᴛʜɪꜱ ʙᴏᴛ ᴀʟꜱᴏ ꜱᴜᴘᴘᴏʀᴛꜱ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ."""
        await message.reply_photo(
            photo=PICS,
            caption=txt,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/CinemaVenoOfficial")
                    ],
                    [
                        InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help')
                    ]
                ]
            )
        )
        return
    if id:
        if old == True:
            try:
                await client.send_message(id, "ʏᴏᴜʀ ꜰʀɪᴇɴᴅ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴜꜱɪɴɢ ᴏᴜʀ ʙᴏᴛ")
                await message.reply_photo(
                    photo=PICS,
                    caption=txt,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/CinemaVenoOfficial")
                            ],
                            [
                                InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help')
                            ]
                        ]
                    )
                )
            except:
                return
        else:
            await client.send_message(id, "Congrats! You Won 10GB Upload limit")
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 10737418240
            uploadlimit(int(id), new_limit)
            await message.reply_text(text=f"""ʜᴇʟʟᴏ {wish} {message.from_user.first_name } \n\n
➻ ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ʏᴇᴛ ᴘᴏᴡᴇʀꜰᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ. \n
➻ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ʏᴏᴜʀ ꜰɪʟᴇꜱ\n
➻ ʏᴏᴜ ᴄᴀɴ ᴀʟꜱᴏ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ ᴛᴏ ꜰɪʟᴇ ᴀɴᴅ ꜰɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ.\n 
➻ ᴛʜɪꜱ ʙᴏᴛ ᴀʟꜱᴏ ꜱᴜᴘᴘᴏʀᴛꜱ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.""", reply_to_message_id=message.id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/CinemaVenoOfficial")
                    ],
                    [
                        InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help')
                    ]
                ]
            )
        )

@Client.on_callback_query(filters.regex(r"^help$"))
async def help_callback_handler(_, query):
    loading_placeholder = "◌◌◌"
    
    # Edit the original message with the loading placeholder
    await query.message.edit_text(
        text=loading_placeholder,
        parse_mode=enums.ParseMode.HTML
    )
    for _ in range(3):
        await asyncio.sleep(0.2)  # Simulating loading delay
        loading_placeholder = loading_placeholder.replace("◌", "●", 1)
        await query.message.edit_text(
            text=loading_placeholder,
            parse_mode=enums.ParseMode.HTML
        )
        
    buttons = [
        [
            InlineKeyboardButton('ᴛʜᴜᴍʙɴᴀɪʟ', callback_data='thumbnail'),
            InlineKeyboardButton('ᴄᴀᴘᴛɪᴏɴ', callback_data='caption')
        ],
        [
            InlineKeyboardButton('ʀᴇɴᴅᴇʀɪɴɢ ɪɴꜰᴏ', callback_data='render')
        ],
        [
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ꜱᴏᴜʀᴄᴇ', callback_data='source')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=script.HELP_TXT.format(query.from_user.mention),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )

    
@Client.on_callback_query(filters.regex(r"^caption$"))
async def caption_callback_handler(_, query):
    buttons = [
        [InlineKeyboardButton('Back', callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=script.CAPTION_TXT,
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )
    
@Client.on_callback_query(filters.regex(r"^thumbnail$"))
async def thumbnail_callback_handler(_, query):
    buttons = [
        [InlineKeyboardButton('Back', callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=script.THUMBNAIL_TXT,
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )
    
@Client.on_callback_query(filters.regex(r"^home$"))
async def home_callback_handler(_, query):
    home_text = f"""ʜᴇʟʟᴏ {wish} {query.from_user.first_name} \n\n
➻ ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ʏᴇᴛ ᴘᴏᴡᴇʀꜰᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ.\n
➻ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ʏᴏᴜʀ ꜰɪʟᴇꜱ\n
➻ ʏᴏᴜ ᴄᴀɴ ᴀʟꜱᴏ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ ᴛᴏ ꜰɪʟᴇ ᴀɴᴅ ꜰɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ.\n 
➻ ᴛʜɪꜱ ʙᴏᴛ ᴀʟꜱᴏ ꜱᴜᴘᴘᴏʀᴛꜱ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ."""
    
    buttons = [
        [
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/CinemaVenoOfficial")
        ],
        [
                InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url='https://t.me/+9Y0zeiIAFeczMDJl'),
                InlineKeyboardButton("ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ", url='https://t.me/CinemaVenoOfficial')
        ],
        [
                InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help')
        ]
    ]    
    reply_markup = InlineKeyboardMarkup(buttons)    
    await query.message.edit_text(text=home_text, reply_markup=reply_markup)
 
@Client.on_callback_query(filters.regex(r"^render$"))
async def render_callback_handler(_, query):
    render_text = f"""ꜱʏꜱᴛᴇᴍ ꜱᴛᴀᴛᴜꜱ 

❂ ʀᴀᴍ: {"●" * random.randint(3, 4) + "◌" * (5 - random.randint(3, 4))}
✤ ᴄᴘᴜ: {"●" * random.randint(3, 5) + "◌" * (5 - random.randint(3, 5))}
✪ ᴅᴀᴛᴀ: {"●" * random.randint(2, 5) + "◌" * (5 - random.randint(2, 5))}

ᴠ[2.3.4] ꜱᴛᴀʙʟᴇ"""
    
    await query.answer(text=render_text, show_alert=True)
    
@Client.on_callback_query(filters.regex(r"^source$"))
async def source_callback_handler(_, query):
    buttons = [
        [InlineKeyboardButton('Back', callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=script.SOURCE_TXT,
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )

@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    update_channel = CHANNEL
    user_id = message.from_user.id
    if update_channel:
        try:
            await client.get_chat_member(update_channel, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text(
                "**__ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ꜱᴜʙꜱᴄʀɪʙᴇᴅ ᴍʏ ᴄʜᴀɴɴᴇʟ__** ",
                 reply_to_message_id=message.id,
                 reply_markup=InlineKeyboardMarkup(
                     [
                        [
                            InlineKeyboardButton("⏫ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ⏫", url=f"https://t.me/CinemaVenoOfficial")
                        ]
                     ]
                 )
            )
            await client.send_message(
                LOG_CHANNEL,f"#new_user,\n\n**ID** : `{user_id}`\n**Name**: {message.from_user.first_name} {message.from_user.last_name}\n**User-Plan** : {user}\n\n ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔖 Restrict User ( **pm** ) 🔖", callback_data="ceasepower")
                        ]
                    ]
                )
            )
            return
    try:
        bot_data = find_one(int(botid))
        prrename = bot_data['total_rename']
        prsize = bot_data['total_size']
        user_deta = find_one(user_id)
    except:
        await message.reply_text("Use About cmd first /about")
    try:
        used_date = user_deta["date"]
        buy_date = user_deta["prexdate"]
        daily = user_deta["daily"]
        user_type = user_deta["usertype"]
    except:
        await message.reply_text(
            text=f"ʜᴇʟʟᴏ dear {message.from_user.first_name}  **we are currently working on this issue**\n\nPlease try to rename files from your another account.\nBecause this BOT can't rename file sent by some ids.\n\nIf you are an **ADMINS** Don't worry ! here we have a solution for you dear {message.from_user.first_name }.\n\nPlease use \n🎗️ `/addpremium your_other_userid` 🆔 to use premium feautres\n\n",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/CinemaVenoOfficial")
                    ],
                    [   InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url='https://t.me/+9Y0zeiIAFeczMDJl'),
                        InlineKeyboardButton("ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ", url='https://t.me/CinemaVenoOfficial')
                    ],
                    [
                        InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help')
                    ]
                ]
            )
        )
        await message.reply_text(text=f"🦋")
        return 
    c_time = time.time()
    if user_type == "Free":
        LIMIT = 600
    else:
        LIMIT = 50
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"```ꜱᴏʀʀʏ ᴅᴜᴅᴇ ɪ ᴀᴍ ɴᴏᴛ ᴏɴʟʏ ꜰᴏʀ ʏᴏᴜ \n ꜰʟᴏᴏᴅ ᴄᴏɴᴛʀᴏʟ ɪꜱ ᴀᴄᴛɪᴠᴇ ꜱᴏ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ꜰᴏʀ {ltime}```", reply_to_message_id=message.id)
    else:
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        value = 4294967296
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"100% ᴏꜰ ᴅᴀɪʟʏ {humanbytes(limit)} ᴅᴀᴛᴀ Qᴜᴏᴛᴀ ᴇxʜᴀᴜꜱᴛᴇᴅ.\n\n  ꜰɪʟᴇ ꜱɪᴢᴇ ᴅᴇᴛᴇᴄᴛᴇᴅ {humanbytes(file.file_size)}\n  ᴜꜱᴇᴅ ᴅᴀɪʟʏ ʟɪᴍɪᴛ {humanbytes(used)}\n\nʏᴏᴜ ʜᴀᴠᴇ ᴏɴʟʏ **{humanbytes(remain)}** ʟᴇꜰᴛ ᴏɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.\nɪꜰ ᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇɴᴀᴍᴇ ʟᴀʀɢᴇ ꜰɪʟᴇ ᴜᴘɢʀᴀᴅᴇ ʏᴏᴜʀ ᴘʟᴀɴ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ 💰💳", callback_data="upgrade")]]))
            return
        if value < file.file_size:
            
            if STRING:
                if buy_date == None:
                    await message.reply_text(f"ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ᴍᴏʀᴇ ᴛʜᴇɴ {humanbytes(limit)} ᴜꜱᴇᴅ ᴅᴀɪʟʏ ʟɪᴍɪᴛ {humanbytes(used)} ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ 💰💳", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪꜱ ꜰɪʟᴇ?\n**ꜰɪʟᴇ ɴᴀᴍᴇ** :- `{filename}`\n\n**ꜰɪʟᴇ ꜱɪᴢᴇ** :- {humanize.naturalsize(file.file_size)}\n**ᴅᴄ ɪᴅ** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 ʀᴇɴᴀᴍᴇ", callback_data="rename"), InlineKeyboardButton("⏳ ᴄᴀɴᴄᴇʟ", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 16384000000)
                    usertype(message.from_user.id, "Free")
                    await message.reply_text(f'ʏᴏᴜʀ ᴘʟᴀɴ ᴇxᴘɪʀᴇᴅ ᴏɴ {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ꜰɪʟᴇꜱ ʙɪɢɢᴇʀ ᴛʜᴀɴ 2ɢʙ")
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 16384000000)
                    usertype(message.from_user.id, "Free")
            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(
                f"""ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪꜱ ꜰɪʟᴇ?\n**ꜰɪʟᴇ ɴᴀᴍᴇ** :- `{filename}`\n\n**ꜰɪʟᴇ ꜱɪᴢᴇ** :- {filesize}\n**ᴅᴄ ɪᴅ** :- {dcid}""", 
                reply_to_message_id=message.id, 
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📝 ʀᴇɴᴀᴍᴇ", callback_data="rename"),
                            InlineKeyboardButton("⏳ ᴄᴀɴᴄᴇʟ", callback_data="cancel")
                        ]
                    ]
                )
            )

	    
