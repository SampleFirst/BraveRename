import random

class script(object):
    SOURCE_TXT = """<b>ɴᴏᴛᴇ:</b>
- Updated Source - <a href=https://t.me/CinemaVenoOfficial>ɴᴏᴋɪ ɪʀɴᴏ</a>"""

    RENDER_TXT = f"""<b>ɴᴏᴛᴇ:</b>
 🌐 SYSTEM STATUS 🌐

📊 RAM: {"●" * random.randint(0, 5) + "○" * (5 - random.randint(0, 5))}
⚙️ CPU: {"●" * random.randint(0, 5) + "○" * (5 - random.randint(0, 5))}
📈 Data: {"●" * random.randint(0, 5) + "○" * (5 - random.randint(0, 5))}

{"●" * random.randint(0, 2) + "○" * (2 - random.randint(0, 2))}

v[2.3.4] stable"""

    HELP_TXT = """𝙷𝙴𝚈 {}
Updated Help Text."""

    THUMBNAIL_TXT = """<b>ɴᴏᴛᴇ:</b>
 🌌How to Set Thumbnail\n\n
Send any photo to me, and I will save it automatically.
/delthumb : Use this command to delete old thumbnail. 
/viewthumb : Use this command to view your current thumbnail."""

    CAPTION_TXT = """<b>ɴᴏᴛᴇ:</b>
📝 How to Set Caption\n\n
/set_caption Set a custom caption for your content.
/see_caption: To view your custom caption.
/delete_caption: Remove your custom caption from my DB."""

    START_TXT = """Hello {wish} {message.from_user.first_name } \n\n
➻ This is an advanced and yet powerful rename bot. 
➻ Using this bot you can rename and change thumbnail of your files. 
➻ You can also convert video to file and file to video. 
➻ This bot also supports custom thumbnail and custom caption."""
