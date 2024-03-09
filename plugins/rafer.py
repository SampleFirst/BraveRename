from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client, message):
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Share Your Link", url=f"https://t.me/share/url?url=https://t.me/Zoro_Renamer_bot?start={message.from_user.id}")
            ]
        ]
    )
    await message.reply_text("Refer And Earn Get 10GB Upload Limit\nPer Refer 10GB", reply_to_message_id=message.message_id, reply_markup=reply_markup)
