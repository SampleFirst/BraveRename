import random

class script(object):
    START_TEXT = """ʜᴇʏ! {},\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ"""
    SOURCE_TEXT = """<b>Note:</b>\n- ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ ɪꜱ ɴᴏᴛ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ"""
    RENDER_TEXT = f"""<b>ɴᴏᴛᴇ:</b>
 🌐 SYSTEM STATUS 🌐

📊 RAM: {"●" * random.randint(0, 5) + "○" * (5 - random.randint(0, 5))}
⚙️ CPU: {"●" * random.randint(0, 5) + "○" * (5 - random.randint(0, 5))}
📈 Data: {"●" * random.randint(0, 5) + "○" * (5 - random.randint(0, 5))}

{"●" * random.randint(0, 2) + "○" * (2 - random.randint(0, 2))}

v[2.3.4] stable"""
    HELP_TEXT = """ʜᴇʏ\nᴜᴘᴅᴀᴛᴇᴅ ʜᴇʟᴘ ᴛᴇxᴛ."""
    ABOUT_TEXT = """ʜᴇʏ\nᴜᴘᴅᴀᴛᴇᴅ ᴀʙᴏᴜᴛ ᴛᴇxᴛ."""
    THUMBNAIL_TEXT = """<b>Note:</b>\n🌌How to Set Thumbnail\n\nSend any photo to me, and I will save it automatically.\n/delthumb : Use this command to delete old thumbnail. \n/viewthumb : Use this command to view your current thumbnail."""
    CAPTION_TEXT = """<b>Note:</b>\n📝 How to Set Caption\n\n/set_caption Set a custom caption for your content.\n/see_caption: To view your custom caption.\n/delete_caption: Remove your custom caption from my DB."""
    WONX_TEXT = """ʏᴏᴜʀ ꜰʀɪᴇɴᴅ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴜꜱɪɴɢ ᴏᴜʀ ʙᴏᴛ"""
    WON_TEXT = """🎉 ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴꜱ! ʏᴏᴜ ᴡᴏɴ 10ɢʙ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ"""
    SUB_TEXT = """🔒 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ꜰᴏʀ ᴜꜱɪɴɢ ʙᴏᴛ"""
    LOG_TEXT = """#New_User\nUSER_ID = {user_id}\nNAME = {message.from_user.mention}\nPLAN = {user}"""
    FLOOD_TEXT = """ꜰʟᴏᴏᴅ ᴄᴏɴᴛʀᴏʟ ɪꜱ ᴀᴄᴛɪᴠᴇ ꜱᴏ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ꜰᴏʀ {ltime}"""
    EXP_QUOTA_TEXT = """100% ᴏꜰ ᴅᴀɪʟʏ {humanbytes(limit)} ᴅᴀᴛᴀ Qᴜᴏᴛᴀ ᴇxʜᴀᴜꜱᴛᴇᴅ.\nꜰɪʟᴇ ꜱɪᴢᴇ ᴅᴇᴛᴇᴄᴛᴇᴅ {humanbytes(file.file_size)}\nᴜꜱᴇᴅ ᴅᴀɪʟʏ ʟɪᴍɪᴛ {humanbytes(used)}\nʏᴏᴜ ʜᴀᴠᴇ ᴏɴʟʏ **{humanbytes(remain)}** ʟᴇꜰᴛ ᴏɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.\nɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇɴᴀᴍᴇ ʟᴀʀɢᴇ ꜰɪʟᴇ ᴜᴘɢʀᴀᴅᴇ ʏᴏᴜʀ ᴘʟᴀɴ."""
    DLIMIT_TEXT = """ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ᴍᴏʀᴇ ᴛʜᴀɴ {humanbytes(limit)} ᴜꜱᴇᴅ ᴅᴀɪʟʏ ʟɪᴍɪᴛ {humanbytes(used)}"""
    RENAME_TEXT = """ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪꜱ ꜰɪʟᴇ?\n\n**File Name**: `{a}`\n**File Size**: {b}\n**DC ID**: {c}"""
    EXP_TEXT = """ʏᴏᴜʀ ᴘʟᴀɴ ᴇxᴘɪʀᴇᴅ ᴏɴ {buy_date}"""
    GB_TEXT = """ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ꜰɪʟᴇꜱ ʙɪɢɢᴇʀ ᴛʜᴀɴ 2ɢʙ"""
    ALIVE_TEXT = """
ʜᴇʟʟᴏ 👋, {user}\n
ᴠᴇʀꜱɪᴏɴ: ♻️ {bot_version}\n
ʙᴏᴛ ʀᴜɴᴛɪᴍᴇ: ⏳ {elapsed_time_formatted}"""

