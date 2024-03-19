from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
import asyncio

@Client.on_message(filters.command("upgrade"))
async def upgrade(bot, update):
    message = await update.reply_text("This Feature coming soon...")
    await asyncio.sleep(20)
    try:
        await message.delete()
        await update.delete()
    except Exception as e:
        print(f"An error occurred: {e}")
      
