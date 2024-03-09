import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.database import find_one, used_limit, daily, uploadlimit, usertype
from helper.date import check_expi
from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["myplan"]))
async def myplan(client, message):
    user_data = find_one(message.from_user.id)
    limit = user_data["uploadlimit"]
    used = user_data["used_limit"]
    user_type = user_data["usertype"]
    pre_expiration = user_data["prexdate"]

    if pre_expiration:
        pre_check = check_expi(pre_expiration)
        if not pre_check:
            uploadlimit(message.from_user.id, 16384000000)
            usertype(message.from_user.id, "Free")

    if pre_expiration is None or check_expi(pre_expiration) is False:
        today = int(time.mktime(time.strptime(str(date.today()), '%Y-%m-%d')))
        daily(message.from_user.id, today)
        used_limit(message.from_user.id, 0)

    remain = limit - used
    normal_date = None
    if pre_expiration:
        normal_date = datetime.fromtimestamp(pre_expiration).strftime('%Y-%m-%d')

    text = f"User ID:- `{message.from_user.id}`\nPlan :- {user_type}\nDaily Upload Limit :- {humanbytes(limit)}\nToday Used :- {humanbytes(used)}\nRemain:- {humanbytes(remain)}"
    if normal_date:
        text += f"\n\nYour Plan Ends On :- {normal_date}"

    reply_markup = None
    if user_type == "Free":
        reply_markup = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("💳 Upgrade", callback_data="upgrade"),
                InlineKeyboardButton("Cancel ✖️ ", callback_data="cancel")
            ]
        ]
    )
    await message.reply(text, quote=True, reply_markup=reply_markup)
