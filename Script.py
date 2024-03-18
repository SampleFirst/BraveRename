import random

class script(object):
    START_TEXT = """ʜᴇʏ! {},\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ"""
    SOURCE_TEXT = """<b>ɴᴏᴛᴇ:</b>\n- ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ ɪꜱ ɴᴏᴛ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ"""
    RENDER_TEXT = f"""<b>ɴᴏᴛᴇ:</b>
 🌐 SYSTEM STATUS 🌐

📊 RAM: {"●" * random.randint(0, 5) + "○" * (5 - random.randint(0, 5))}
⚙️ CPU: {"●" * random.randint(0, 5) + "○" * (5 - random.randint(0, 5))}
📈 Data: {"●" * random.randint(0, 5) + "○" * (5 - random.randint(0, 5))}

{"●" * random.randint(0, 2) + "○" * (2 - random.randint(0, 2))}

v[2.3.4] stable"""
    HELP_TEXT = """ʜᴇʏ\nᴜᴘᴅᴀᴛᴇᴅ ʜᴇʟᴘ ᴛᴇxᴛ."""
    ABOUT_TEXT = """ʜᴇʏ\nᴜᴘᴅᴀᴛᴇᴅ ᴀʙᴏᴜᴛ ᴛᴇxᴛ."""
    THUMBNAIL_TEXT = """<b>ɴᴏᴛᴇ:</b>\n🌌 ʜᴏᴡ ᴛᴏ ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ\n\n/set_thumb : ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ꜰᴏʀ ʏᴏᴜʀ ᴄᴏɴᴛᴇɴᴛ.\n/view_thumb : ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.\n/del_thumb : ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴏʟᴅ ᴛʜᴜᴍʙɴᴀɪʟ."""
    CAPTION_TEXT = """<b>ɴᴏᴛᴇ:</b>\n📝 ʜᴏᴡ ᴛᴏ ꜱᴇᴛ ᴄᴀᴘᴛɪᴏɴ\n\n/set_caption : ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ꜰᴏʀ ʏᴏᴜʀ ᴄᴏɴᴛᴇɴᴛ.\n/see_caption : ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n/del_caption : ʀᴇᴍᴏᴠᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ꜰʀᴏᴍ ᴍʏ ᴅʙ."""
    WONX_TEXT = """ʏᴏᴜʀ ꜰʀɪᴇɴᴅ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴜꜱɪɴɢ ᴏᴜʀ ʙᴏᴛ"""
    WON_TEXT = """🎉 ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴꜱ! ʏᴏᴜ ᴡᴏɴ 10ɢʙ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ"""
    SUB_TEXT = """🔒 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ꜰᴏʀ ᴜꜱɪɴɢ ʙᴏᴛ"""
    LOG_TEXT = """#New_User\nUSER_ID = {user_id}\nNAME = {message.from_user.mention}\nPLAN = {user}"""
    FLOOD_TEXT = """ꜰʟᴏᴏᴅ ᴄᴏɴᴛʀᴏʟ ɪꜱ ᴀᴄᴛɪᴠᴇ ꜱᴏ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ꜰᴏʀ {a}"""
    EXP_QUOTA_TEXT = """100% ᴏꜰ ᴅᴀɪʟʏ {a} ᴅᴀᴛᴀ Qᴜᴏᴛᴀ ᴇxʜᴀᴜꜱᴛᴇᴅ.\nꜰɪʟᴇ ꜱɪᴢᴇ ᴅᴇᴛᴇᴄᴛᴇᴅ {b}\nᴜꜱᴇᴅ ᴅᴀɪʟʏ ʟɪᴍɪᴛ {c}\nʏᴏᴜ ʜᴀᴠᴇ ᴏɴʟʏ **{d}** ʟᴇꜰᴛ ᴏɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.\nɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇɴᴀᴍᴇ ʟᴀʀɢᴇ ꜰɪʟᴇ ᴜᴘɢʀᴀᴅᴇ ʏᴏᴜʀ ᴘʟᴀɴ."""
    DLIMIT_TEXT = """ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ᴍᴏʀᴇ ᴛʜᴀɴ {a} ᴜꜱᴇᴅ ᴅᴀɪʟʏ ʟɪᴍɪᴛ {b}"""
    RENAME_TEXT = """ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪꜱ ꜰɪʟᴇ?\n\n**File Name**: `{a}`\n**File Size**: {b}\n**DC ID**: {c}"""
    EXP_TEXT = """ʏᴏᴜʀ ᴘʟᴀɴ ᴇxᴘɪʀᴇᴅ ᴏɴ {a}"""
    GB_TEXT = """ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ꜰɪʟᴇꜱ ʙɪɢɢᴇʀ ᴛʜᴀɴ 2ɢʙ"""
    ALIVE_TEXT = """
ʜᴇʟʟᴏ 👋, {a}\n
ᴠᴇʀꜱɪᴏɴ: ♻️ {b}\n
ʙᴏᴛ ʀᴜɴᴛɪᴍᴇ: ⏳ {c}"""
    SELECT_FILETYPE_TEXT = """**ꜱᴇʟᴇᴄᴛ ᴛʜᴇ ᴏᴜᴛᴘᴜᴛ ꜰɪʟᴇ ᴛʏᴘᴇ**\n\n**ɴᴇᴡ ɴᴀᴍᴇ** :- {out_filename}"""
    

