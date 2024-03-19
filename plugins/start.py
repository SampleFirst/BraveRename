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


@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    loading_sticker_message = await message.reply_sticker("CAACAgUAAxkBAAEKDf1k3mCOA5HUO51nPYSN-yaCNFj1PQAC7QoAAgEFoFRUQkvwYhdUWTAE")
    await asyncio.sleep(2)
    await loading_sticker_message.delete()
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        await message.reply_photo(
            photo=PICS,
            caption=script.START_TEXT.format(message.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔄 ᴜᴘᴅᴀᴛᴇ", url=(UPDATE_CHANNEL)),
                        InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ", url=(SUPPORT_CHAT)),
                    ],
                    [
                        InlineKeyboardButton("❓ ʜᴇʟᴘ", callback_data='help'),
                        InlineKeyboardButton("ℹ️ ᴀʙᴏᴜᴛ", callback_data='about')
                    ]
                ]
            )
        )
        return
    if id:
        if old:
            try:
                await client.send_message(id, script.WONX_TEXT)
                await message.reply_photo(
                    photo=PICS,
                    caption=script.START_TEXT.format(message.from_user.mention),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔄 ᴜᴘᴅᴀᴛᴇ", url=(UPDATE_CHANNEL)),
                                InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ", url=(SUPPORT_CHAT)),
                            ],
                            [
                                InlineKeyboardButton("❓ ʜᴇʟᴘ", callback_data='help'),
                                InlineKeyboardButton("ℹ️ ᴀʙᴏᴜᴛ", callback_data='about')
                            ]
                        ]
                    )
                )
            except:
                return
        else:
            await client.send_message(id, script.WON_TEXT)
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 10737418240
            uploadlimit(int(id), new_limit)
            await message.reply_text(
                caption=script.START_TEXT.format(message.from_user.mention), 
                reply_to_message_id=message.id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄 ᴜᴘᴅᴀᴛᴇ", url=(UPDATE_CHANNEL))
                        ],
                        [
                            InlineKeyboardButton("❓ ʜᴇʟᴘ", callback_data='help')
                        ]
                    ]
                )
            )

@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))

@Client.on_callback_query(filters.regex(r"^help$"))
async def help_callback_handler(client, query):
    loading_placeholder = "◌◌◌"
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
            InlineKeyboardButton("🌌 ᴛʜᴜᴍʙɴᴀɪʟ", callback_data='thumbnail'),
            InlineKeyboardButton("📝 ᴄᴀᴘᴛɪᴏɴ", callback_data='caption')
        ],
        [
            InlineKeyboardButton("⬅️ ʜᴏᴍᴇ", callback_data='home'),
            InlineKeyboardButton("ℹ️ ᴀʙᴏᴜᴛ", callback_data='about')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=script.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )


@Client.on_callback_query(filters.regex(r"^about$"))
async def about_callback_handler(client, query):
    loading_placeholder = "◌◌◌"
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
            InlineKeyboardButton("ℹ️ ᴀʙᴏᴜᴛ", callback_data='about'),
            InlineKeyboardButton("⬅️ ʜᴏᴍᴇ", callback_data='home')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=script.ABOUT_TEXT,
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )


@Client.on_callback_query(filters.regex(r"^caption$"))
async def caption_callback_handler(client, query):
    loading_placeholder = "◌◌◌"
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
            InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data='help')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=script.CAPTION_TEXT,
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )


@Client.on_callback_query(filters.regex(r"^thumbnail$"))
async def thumbnail_callback_handler(client, query):
    loading_placeholder = "◌◌◌"
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
            InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data='help')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=script.THUMBNAIL_TEXT,
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )


@Client.on_callback_query(filters.regex(r"^home$"))
async def home_callback_handler(client, query):
    loading_placeholder = "◌◌◌"
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
            InlineKeyboardButton("🔄 ᴜᴘᴅᴀᴛᴇ", url=(UPDATE_CHANNEL)),
            InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ", url=(SUPPORT_CHAT)),
        ],
        [
            InlineKeyboardButton("❓ ʜᴇʟᴘ", callback_data='help'),
            InlineKeyboardButton("ℹ️ ᴀʙᴏᴜᴛ", callback_data='about')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(text=script.START_TEXT.format(query.from_user.mention), reply_markup=reply_markup)


@Client.on_callback_query(filters.regex(r"^render$"))
async def render_callback_handler(client, query):
    loading_placeholder = "◌◌◌"
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
    await query.answer(text=script.RENDER_TEXT, show_alert=True)


@Client.on_callback_query(filters.regex(r"^source$"))
async def source_callback_handler(client, query):
    loading_placeholder = "◌◌◌"
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
            InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data='help')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=script.SOURCE_TEXT,
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
                text=script.SUB_TEXT.format(message.from_user.mention),
                reply_to_message_id=message.id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔓 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=(UPDATE_CHANNEL))
                        ]
                    ]
                )
            )
            await client.send_message(
                LOG_CHANNEL,
                text=script.LOG_TEXT.format(user_id, message.from_user.mention, user),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔖 ʀᴇꜱᴛʀɪᴄᴛ ᴜꜱᴇʀ ( **pm** )", callback_data="ceasepower")
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
            text=script.START_TEXT.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔄 ᴜᴘᴅᴀᴛᴇ", url=(UPDATE_CHANNEL)),
                        InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ", url=(SUPPORT_CHAT)),
                    ],
                    [
                        InlineKeyboardButton("❓ ʜᴇʟᴘ", callback_data='help'),
                        InlineKeyboardButton("ℹ️ ᴀʙᴏᴜᴛ", callback_data='about')
                    ]
                ]
            )
        )

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
        await message.reply_text(
            text=script.FLOOD_TEXT.format(a=ltime), 
            reply_to_message_id=message.id
        )
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
            await message.reply_text(
                text=script.EXP_QUOTA_TEXT.format(a=humanbytes(limit), b=humanbytes(file.file_size), c=humanbytes(used), d=humanbytes(remain)),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ 💳", callback_data="upgrade")
                        ]
                    ]
                )
            )
            return
        if value < file.file_size:

            if STRING:
                if buy_date == None:
                    await message.reply_text(
                        text=script.DLIMIT_TEXT.format(a=humanbytes(limit), b=humanbytes(used)),
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ 💳", callback_data="upgrade")
                                ]
                            ]
                        )
                    )
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(
                        text=script.RENAME_TEXT.format(a=filename, b=humanize.naturalsize(file.file_size), c=dcid),
                        reply_to_message_id=message.id,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton("📝 ʀᴇɴᴀᴍᴇ", callback_data="rename"),
                                ],
                                [
                                    InlineKeyboardButton("❌ ᴄᴀɴᴄᴇʟ ❌", callback_data="cancel")
                                ]
                            ]
                        )
                    )
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 16384000000)
                    usertype(message.from_user.id, "Free")
                    await message.reply_text(
                        text=script.EXP_TEXT.format(a=buy_date), 
                        quote=True
                    )
                    return
            else:
                await message.reply_text(
                    text=script.GB_TEXT
                )
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
                text=script.RENAME_TEXT.format(a=filename, b=filesize, c=dcid),
                reply_to_message_id=message.id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📝 ʀᴇɴᴀᴍᴇ", callback_data="rename"),
                        ],
                        [
                            InlineKeyboardButton("❌ ᴄᴀɴᴄᴇʟ ❌", callback_data="cancel")
                        ]
                    ]
                )
            )
            

