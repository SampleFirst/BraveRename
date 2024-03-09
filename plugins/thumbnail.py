from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def view_thumb(client, message):
    print(message.chat.id)
    thumb = find(int(message.chat.id))[0]
    if thumb:
        await client.send_photo(message.chat.id, photo=thumb)
    else:
        await message.reply_text("**You don't have any thumbnail**")

@Client.on_message(filters.private & filters.command(['delthumb']))
async def remove_thumb(client, message):
    delthumb(int(message.chat.id))
    await message.reply_text("**Thumbnail deleted successfully**")

@Client.on_message(filters.private & filters.photo)
async def add_thumbs(client, message):
    file_id = str(message.photo.file_id)
    addthumb(message.chat.id, file_id)
    await message.reply_text("**Thumbnail saved successfully** ✅")

