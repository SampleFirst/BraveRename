from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb

# Global variable to track if user has set thumbnail or not
user_thumbnail_set = {}

@Client.on_message(filters.private & filters.command(['set_thumb']))
async def set_thumbnail_command(client, message):
    user_id = message.from_user.id
    user_thumbnail_set[user_id] = True
    await message.reply_text("ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ᴘʜᴏᴛᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ꜱᴇᴛ ᴀꜱ ᴛʜᴜᴍʙɴᴀɪʟ.")

@Client.on_message(filters.private & filters.photo)
async def add_thumbs(client, message):
    user_id = message.from_user.id
    if user_id not in user_thumbnail_set or not user_thumbnail_set[user_id]:
        return
    
    if file_id = str(message.photo.file_id)
        addthumb(user_id, file_id)
        user_thumbnail_set[user_id] = False
        await message.reply_text("ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴇᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ! ✅", quote=True)
    else:
        user_thumbnail_set[user_id] = False
        await message.reply_text("ʜᴇʏ ᴜꜱᴇʀ ᴛʜɪꜱ ɴᴏᴛ ᴀ ᴘʜᴏᴛᴏ ꜰᴏʀ ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ! 🤔", quote=True)
    
@Client.on_message(filters.private & filters.command(['view_thumb']))
async def view_thumb(client, message):
    user_id = message.from_user.id
    thumb = find(user_id)[0]
    if thumb:
        await client.send_photo(user_id, photo=thumb, quote=True)
    else:
        await message.reply_text("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴇᴛ**", quote=True)

@Client.on_message(filters.private & filters.command(['del_thumb']))
async def remove_thumb(client, message):
    user_id = message.from_user.id
    delthumb(user_id)
    await message.reply_text("**ᴛʜᴜᴍʙɴᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ**", quote=True)
    
