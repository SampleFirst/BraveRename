from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit, usertype, addpre

ADMINS = int(os.environ.get("ADMINS", ))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

@Client.on_message(filters.private & filters.user(ADMINS) & filters.command("warn"))
async def warn(c, m):
    if len(m.command) >= 3:
        try:
            user_id = m.text.split(' ', 2)[1]
            reason = m.text.split(' ', 2)[2]
            await m.reply_text("User Notified Successfully")
            await c.send_message(chat_id=int(user_id), text=reason)
        except:
            await m.reply_text("User Not Notified Successfully 😔")

@Client.on_message(filters.private & filters.user(ADMINS) & filters.command("addpremium"))
async def buypremium(bot, message):
    await message.reply_text("🦋 Select Plan to upgrade...", quote=True, reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("🪙 Silver", callback_data="vip1")],
        [InlineKeyboardButton("💫Gold", callback_data="vip2")],
        [InlineKeyboardButton("💎 Diamond", callback_data="vip3")]
    ]))

@Client.on_message((filters.channel | filters.private) & filters.user(ADMINS) & filters.command("ceasepower"))
async def ceasepremium(bot, message):
    await message.reply_text("POWER CEASE MODE", quote=True, reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("•× Limit 5.0GB ×•", callback_data="cp1"),
         InlineKeyboardButton("•× Limit 2.4GB ×•", callback_data="cp2")],
        [InlineKeyboardButton("•••× CEASE ALL POWER ×•••", callback_data="cp3")]
    ]))

@Client.on_message((filters.channel | filters.private) & filters.user(ADMINS) & filters.command("resetpower"))
async def resetpower(bot, message):
    await message.reply_text(text=f"ᴅᴏ ʏᴏᴜ ʀᴇᴀʟʟʏ ᴡᴀɴᴛ ᴛᴏ ʀᴇꜱᴇᴛ ᴅᴀɪʟʏ ʟɪᴍɪᴛ ᴛᴏ ᴅᴇꜰᴀᴜʟᴛ ᴅᴀᴛᴀ ʟɪᴍɪᴛ 15.25ɢʙ ?",quote=True,reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("• YES ! Set as Default •",callback_data = "dft")],
        [InlineKeyboardButton("❌ Cancel ❌",callback_data = "cancel")]
    ]))

@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot, update):
    id = update.message.reply_to_message.text.split("/addpremium")
    user_id = id[1].replace(" ", "")
    inlimit = 10737418240
    uploadlimit(int(user_id),10737418240)
    usertype(int(user_id),"🪙 **SILVER**")
    addpre(int(user_id))
    await update.message.edit("ᴀᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 10 ɢʙ")
    await bot.send_message(user_id,"ʏᴏᴜ ᴀʀᴇ ᴜᴘɢʀᴀᴅᴇᴅ ᴛᴏ ꜱɪʟᴠᴇʀ. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan")
    await bot.send_message(LOG_CHANNEL,f"⚡️ ᴘʟᴀɴ ᴜᴘɢʀᴀᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 💥\n\nʜᴇʏ ʏᴏᴜ ᴀʀᴇ ᴜᴘɢʀᴀᴅᴇᴅ ᴛᴏ ꜱɪʟᴠᴇʀ. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan")

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot, update):
    id = update.message.reply_to_message.text.split("/addpremium")
    user_id = id[1].replace(" ", "")
    inlimit = 53687091200
    uploadlimit(int(user_id), 53687091200)
    usertype(int(user_id),"💫 **GOLD**")
    addpre(int(user_id))
    await update.message.edit("ᴀᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 50 ɢʙ")
    await bot.send_message(user_id,"ʜᴇʏ ʏᴏᴜ ᴀʀᴇ ᴜᴘɢʀᴀᴅᴇᴅ ᴛᴏ ɢᴏʟᴅ. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan")

@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot, update):
    id = update.message.reply_to_message.text.split("/addpremium")
    user_id = id[1].replace(" ", "")
    inlimit = 107374182400
    uploadlimit(int(user_id), 107374182400)
    usertype(int(user_id),"💎 **DIAMOND**")
    addpre(int(user_id))
    await update.message.edit("ᴀᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 100 ɢʙ")
    await bot.send_message(user_id,"ʜᴇʏ ʏᴏᴜ ᴀʀᴇ ᴜᴘɢʀᴀᴅᴇᴅ ᴛᴏ ᴅɪᴀᴍᴏɴᴅ. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan")

# CEASE POWER MODE @LAZYDEVELOPER

@Client.on_callback_query(filters.regex('cp1'))
async def cp1(bot, update):
    id = update.message.reply_to_message.text.split("/ceasepower")
    user_id = id[1].replace(" ", "")
    inlimit = 5368709120
    uploadlimit(int(user_id),5368709120)
    usertype(int(user_id),"**ACCOUNT DOWNGRADED**")
    addpre(int(user_id))
    await update.message.edit("ᴀᴄᴄᴏᴜɴᴛ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ\nᴛʜᴇ ᴜꜱᴇʀ ᴄᴀɴ ᴏɴʟʏ ᴜꜱᴇ 5.0ɢʙ/ᴅᴀʏ ꜰʀᴏᴍ ᴅᴀᴛᴀ Qᴏᴛᴀ")
    await bot.send_message(user_id,"⚠️ ᴡᴀʀɴɪɴɢ ⚠️\n\n- ᴀᴄᴄᴏᴜɴᴛ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ\nʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴜꜱᴇ 5.0ɢʙ/ᴅᴀʏ ꜰʀᴏᴍ ᴅᴀᴛᴀ Qᴏᴛᴀ.\nᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ - /myplan\n- ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ 🦋<a href='https://t.me/HexaSupportOfficial'>**Zoro**</a>🦋")

@Client.on_callback_query(filters.regex('cp2'))
async def cp2(bot, update):
    id = update.message.reply_to_message.text.split("/ceasepower")
    user_id = id[1].replace(" ", "")
    inlimit = 2574269184
    uploadlimit(int(user_id), 2574269184)
    usertype(int(user_id),"**ACCOUNT DOWNGRADED**")
    addpre(int(user_id))
    await update.message.edit("ᴀᴄᴄᴏᴜɴᴛ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ\nᴛʜᴇ ᴜꜱᴇʀ ᴄᴀɴ ᴏɴʟʏ ᴜꜱᴇ 2.4ɢʙ/ᴅᴀʏ ꜰʀᴏᴍ ᴅᴀᴛᴀ Qᴏᴛᴀ")
    await bot.send_message(user_id,"⛔️ ʟᴀꜱᴛ ᴡᴀʀɴɪɴɢ ⛔️\n\n- ᴀᴄᴄᴏᴜɴᴛ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ\nʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴜꜱᴇ 2.4ɢʙ/ᴅᴀʏ ꜰʀᴏᴍ ᴅᴀᴛᴀ Qᴏᴛᴀ.\nᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ - /myplan\n- ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ 🦋<a href='https://t.me/HexaSupportOfficial'>**Zoro**</a>🦋")

@Client.on_callback_query(filters.regex('cp3'))
async def cp3(bot, update):
    id = update.message.reply_to_message.text.split("/ceasepower")
    user_id = id[1].replace(" ", "")
    inlimit = 0
    uploadlimit(int(user_id), 0)
    usertype(int(user_id),"**POWER CEASED !**")
    addpre(int(user_id))
    await update.message.edit("ᴀʟʟ ᴘᴏᴡᴇʀ ᴄᴇᴀꜱᴇᴅ ꜰʀᴏᴍ ᴛʜᴇ ᴜꜱᴇʀ.\n ᴛʜɪꜱ ᴀᴄᴄᴏᴜɴᴛ ʜᴀꜱ 0 ᴍʙ ʀᴇɴᴀᴍɪɴɢ ᴄᴀᴘᴀᴄɪᴛʏ ")
    await bot.send_message(user_id,"🚫 ᴀʟʟ ᴘᴏᴡᴇʀ ᴄᴇᴀꜱᴇᴅ 🚫\n\n- ᴀʟʟ ᴘᴏᴡᴇʀ ʜᴀꜱ ʙᴇᴇɴ ᴄᴇᴀꜱᴇᴅ ꜰʀᴏᴍ ʏᴏᴜ \n ꜰʀᴏᴍ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ'ᴛ ʀᴇɴᴀᴍᴇ ꜰɪʟᴇꜱ ᴜꜱɪɴɢ ᴍᴇ \nᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ - /myplan\n- ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ 🦋<a href='https://t.me/Vishal_dml'>**Zoro**</a>🦋")

@Client.on_callback_query(filters.regex('dft'))
async def dft(bot, update):
    id = update.message.reply_to_message.text.split("/resetpower")
    user_id = id[1].replace(" ", "")
    inlimit = 16384000000 
    uploadlimit(int(user_id), 16384000000)
    usertype(int(user_id),"**Free**")
    addpre(int(user_id))
    await update.message.edit("ᴅᴀɪʟʏ ᴅᴀᴛᴀ ʟɪᴍɪᴛ ʜᴀꜱ ʙᴇᴇɴ ʀᴇꜱᴇᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ. ᴛʜɪꜱ ᴀᴄᴄᴏᴜɴᴛ ʜᴀꜱ ᴅᴇꜰᴀᴜʟᴛ 15.25 ɢʙ ʀᴇɴᴀᴍɪɴɢ ᴄᴀᴘᴀᴄɪᴛʏ ")
    await bot.send_message(user_id,"ʏᴏᴜʀ ᴅᴀɪʟʏ ᴅᴀᴛᴀ ʟɪᴍɪᴛ ʜᴀꜱ ʙᴇᴇɴ ʀᴇꜱᴇᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ.\n\ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ - /myplan\n- ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ 🦋<a href='https://t.me/Vishal_dml'>**Zoro**</a>🦋")
