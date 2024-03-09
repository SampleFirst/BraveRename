import time
from pyrogram import Client, filters


# Start time of the bot
start_time = time.time()

# Function to get the bot version
def get_bot_version():
    # Replace with the code to fetch the bot version from wherever it's stored
    return "1.0.0"

# Function to get the bot runtime
def get_bot_runtime():
    current_time = time.time()
    elapsed_time = current_time - start_time
    return elapsed_time

# Command handler for "/alive"
@Client.on_message(filters.command("alive"))
async def check_alive(_, message):
    elapsed_time_formatted = time.strftime("%H:%M:%S", time.gmtime(get_bot_runtime()))
    bot_version = get_bot_version()

    await message.reply_photo(
        photo="https://i.imgur.com/L0woBZF.jpeg",
        caption=f"┌─❖\n"
                f"│「 𝗛𝗶 👋 」\n"
                "└┬❖\n"
                f"│✑ 𝙃𝙚𝙡𝙡𝙤, 🈂️{message.from_user.mention}\n"
                f"│✑ 𝙑𝙚𝙧𝙨𝙞𝙤𝙣: ♻️{bot_version}\n"
                f"│✑ 𝘽𝙤𝙩 𝙍𝙪𝙣𝙩𝙞𝙢𝙚: 🛰️{elapsed_time_formatted}\n"
                "└───────────────┈ ⳹",
    )

# Command handler for "/ping"
@Client.on_message(filters.command("ping"))
async def ping(_, message):
    start = time.time()
    msg = await message.reply_text("Pinging....")
    end = time.time()
    time_taken_ms = (end - start) * 1000
    await msg.edit(f"Pɪɴɢ\n{time_taken_ms:.3f} ms")

