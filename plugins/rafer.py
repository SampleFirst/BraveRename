from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client, message):
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⚡ ꜱʜᴀʀᴇ ʏᴏᴜʀ ʟɪɴᴋ", url=f"https://t.me/share/url?url=https://t.me/Zoro_Renamer_bot?start={message.from_user.id}")
            ]
        ]
    )
    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://telegra.ph/file/1f1e29702f6cb8fd157e3.jpg",
        caption="ʀᴇꜰᴇʀ ᴀɴᴅ ᴇᴀʀɴ ɢᴇᴛ 5ɢʙ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ\nᴘᴇʀ ʀᴇꜰᴇʀ 5ɢʙ",
        reply_to_message_id=message.message_id, 
        reply_markup=reply_markup,
        quote=True
    )

