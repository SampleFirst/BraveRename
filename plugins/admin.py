from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit, usertype, addpre
from info import ADMINS, LOG_CHANNEL

@Client.on_message(filters.private & filters.user(ADMINS) & filters.command("warn"))
async def warn(client, message):
    if len(message.command) >= 3:
        try:
            user_id = message.text.split(' ', 2)[1]
            reason = message.text.split(' ', 2)[2]
            await message.reply_text("User Notified Successfully")
            await client.send_message(chat_id=int(user_id), text=reason)
        except:
            await message.reply_text("User Not Notified Successfully 😔")

@Client.on_message(filters.private & filters.user(ADMINS) & filters.command("addpremium"))
async def buypremium(Client, message):
    await message.reply_text("Select Plan to upgrade...", quote=True, reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("🪙 Silver", callback_data="vip1")],
        [InlineKeyboardButton("💫 Gold", callback_data="vip2")],
        [InlineKeyboardButton("💎 Diamond", callback_data="vip3")]
    ]))

@Client.on_message((filters.channel | filters.private) & filters.user(ADMINS) & filters.command("ceasepower"))
async def ceasepremium(Client, message):
    await message.reply_text("POWER CEASE MODE", quote=True, reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Limit 5.0GB", callback_data="cp1"),
         InlineKeyboardButton("Limit 2.4GB", callback_data="cp2")],
        [InlineKeyboardButton("CEASE ALL POWER", callback_data="cp3")]
    ]))

@Client.on_message((filters.channel | filters.private) & filters.user(ADMINS) & filters.command("resetpower"))
async def resetpower(Client, message):
    await message.reply_text(text="Do you really want to reset daily limit to default data limit 5GB?", quote=True, reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("•YES! Set as Default", callback_data="dft")],
        [InlineKeyboardButton("❌ Cancel", callback_data="cancel")]
    ]))

@Client.on_callback_query(filters.regex('vip1'))
async def vip1(Client, message):
    id = message.message.reply_to_message.text.split("/addpremium")
    user_id = id[1].replace(" ", "")
    inlimit = 10737418240
    uploadlimit(int(user_id), inlimit)
    usertype(int(user_id), "🪙 SILVER")
    addpre(int(user_id))
    await message.message.edit("Added successfully to premium upload limit 10 GB")
    await Client.send_message(user_id, "You are upgraded to Silver. Check your plan here /myplan")
    await Client.send_message(LOG_CHANNEL, "⚡ Plan upgraded successfully 💥\n\nHey, you are upgraded to Silver.")

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(Client, message):
    id = message.message.reply_to_message.text.split("/addpremium")
    user_id = id[1].replace(" ", "")
    inlimit = 53687091200
    uploadlimit(int(user_id), inlimit)
    usertype(int(user_id), "💫 GOLD")
    addpre(int(user_id))
    await message.message.edit("Added successfully to premium upload limit 50 GB")
    await Client.send_message(user_id, "Hey, you are upgraded to Gold.")

@Client.on_callback_query(filters.regex('vip3'))
async def vip3(Client, message):
    id = message.message.reply_to_message.text.split("/addpremium")
    user_id = id[1].replace(" ", "")
    inlimit = 107374182400
    uploadlimit(int(user_id), inlimit)
    usertype(int(user_id), "💎 DIAMOND")
    addpre(int(user_id))
    await message.message.edit("Added successfully to premium upload limit 100 GB")
    await Client.send_message(user_id, "Hey, you are upgraded to Diamond.")

@Client.on_callback_query(filters.regex('cp1'))
async def cp1(Client, message):
    id = message.message.reply_to_message.text.split("/ceasepower")
    user_id = id[1].replace(" ", "")
    inlimit = 5368709120
    uploadlimit(int(user_id), inlimit)
    usertype(int(user_id), "**ACCOUNT DOWNGRADED**")
    addpre(int(user_id))
    await message.message.edit("Account downgraded\nThe user can only use 5.0 GB/day from data quota")
    await Client.send_message(user_id, "⚠️ Warning ⚠️\n\n- Account downgraded\nYou can only use 5.0 GB/day from data quota. Check your plan here - /myplan\n- Contact admin.")

@Client.on_callback_query(filters.regex('cp2'))
async def cp2(Client, message):
    id = message.message.reply_to_message.text.split("/ceasepower")
    user_id = id[1].replace(" ", "")
    inlimit = 2684354560
    uploadlimit(int(user_id), inlimit)
    usertype(int(user_id), "**ACCOUNT DOWNGRADED**")
    addpre(int(user_id))
    await message.message.edit("Account downgraded\nThe user can only use 2.5 GB/day from data quota")
    await Client.send_message(user_id, "⛔️ Last warning ⛔️\n\n- Account downgraded\nYou can only use 2.4 GB/day from data quota. Check your plan here - /myplan\n- Contact admin.")

@Client.on_callback_query(filters.regex('cp3'))
async def cp3(Client, message):
    id = message.message.reply_to_message.text.split("/ceasepower")
    user_id = id[1].replace(" ", "")
    inlimit = 0
    uploadlimit(int(user_id), inlimit)
    usertype(int(user_id), "**POWER CEASED !**")
    addpre(int(user_id))
    await message.message.edit("All power ceased from the user.\nThis account has 0 MB remaining capacity")
    await Client.send_message(user_id, "🚫 All power ceased 🚫\n\n- All power has been ceased from you\nFrom now you can't rename files using me. Check your plan here - /myplan\n- Contact admin.")

@Client.on_callback_query(filters.regex('dft'))
async def dft(Client, message):
    id = message.message.reply_to_message.text.split("/resetpower")
    user_id = id[1].replace(" ", "")
    inlimit = 5368709120
    uploadlimit(int(user_id), inlimit)
    usertype(int(user_id), "**Free**")
    addpre(int(user_id))
    await message.message.edit("Daily data limit has been reset successfully. This account has default 5GB remaining capacity")
    await Client.send_message(user_id, "Your daily data limit has been reset successfully.\nCheck your plan here - /myplan\n- Contact admin")
