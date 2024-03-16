import random

class script(object):
    START_TEXT = """Hey! {},\nWelcome to the rename bot"""
    SOURCE_TEXT = """<b>Note:</b>\n- Source Project is Not An open Source"""
    RENDER_TEXT = f"""<b>ɴᴏᴛᴇ:</b>
 🌐 SYSTEM STATUS 🌐

📊 RAM: {"●" * random.randint(0, 5) + "○" * (5 - random.randint(0, 5))}
⚙️ CPU: {"●" * random.randint(0, 5) + "○" * (5 - random.randint(0, 5))}
📈 Data: {"●" * random.randint(0, 5) + "○" * (5 - random.randint(0, 5))}

{"●" * random.randint(0, 2) + "○" * (2 - random.randint(0, 2))}

v[2.3.4] stable"""
    HELP_TEXT = """𝙷𝙴𝚈\nUpdated Help Text."""
    ABOUT_TEXT = """𝙷𝙴𝚈\nUpdated About Text."""
    THUMBNAIL_TEXT = """<b>Note:</b>\n🌌How to Set Thumbnail\n\nSend any photo to me, and I will save it automatically.\n/delthumb : Use this command to delete old thumbnail. \n/viewthumb : Use this command to view your current thumbnail."""
    CAPTION_TEXT = """<b>Note:</b>\n📝 How to Set Caption\n\n/set_caption Set a custom caption for your content.\n/see_caption: To view your custom caption.\n/delete_caption: Remove your custom caption from my DB."""
    WONX_TEXT = """ʏᴏᴜʀ ꜰʀɪᴇɴᴅ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴜꜱɪɴɢ ᴏᴜʀ ʙᴏᴛ"""
    WON_TEXT = """🎉 Congratulations! You Won 10GB Upload limit"""
    SUB_TEXT = """🔒 Join update Channel for using bot"""
    LOG_TEXT = """#New_User\nUSER_ID = {user_id}\nNAME = {message.from_user.mention}\nPLAN = {user}"""
    FLOOD_TEXT = """Flood control is active so please wait for {ltime}"""
    EXP_QUOTA_TEXT = """100% of daily {humanbytes(limit)} data quota exhausted.\nFile size detected {humanbytes(file.file_size)}\nUsed daily limit {humanbytes(used)}\nYou have only **{humanbytes(remain)}** left on your account.\nIf you want to rename large file upgrade your plan."""
    DLIMIT_TEXT = """You can't upload more than {humanbytes(limit)} used daily limit {humanbytes(used)}"""
    RENAME_TEXT = """What do you want me to do with this file?\n\n**File Name**: `{filename}`\n**File Size**: {humanize.naturalsize(file.file_size)}\n**DC ID**: {dcid}"""
    EXP_TEXT = """Your plan expired on {buy_date}"""
    GB_TEXT = """Can't upload files bigger than 2GB"""
    
