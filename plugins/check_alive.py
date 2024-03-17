import time
from pyrogram import Client, filters
from Script import script 

# Start time of the bot
start_time = time.time()

def get_bot_version():
    # Replace with the code to fetch the bot version from wherever it's stored
    return "1.0.0"

def get_bot_runtime():
    current_time = time.time()
    elapsed_time = current_time - start_time
    return elapsed_time

@Client.on_message(filters.command("alive"))
async def check_alive(_, message):
    elapsed_time_formatted = time.strftime("%H:%M:%S", time.gmtime(get_bot_runtime()))
    bot_version = get_bot_version()
    await message.reply_photo(
        photo="https://graph.org/file/4c66eed05443c09179a2e.jpg",
        caption=script.ALIVE_TEXT.format(message.from_user.mention, bot_version, elapsed_time_formatted),
        quote=True 
    )
    
@Client.on_message(filters.command("ping"))
async def ping(_, message):
    start = time.time()
    msg = await message.reply_text("ᴘɪɴɢɪɴɢ....", quote=True)
    end = time.time()
    time_taken_ms = (end - start) * 1000
    await msg.edit(f"ᴘɪɴɢ\n{time_taken_ms:.3f} ms")
    
