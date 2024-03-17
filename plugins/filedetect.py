from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from Script import script 

@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    try:
        if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply):
            new_name = message.text
            await message.delete()
            media = await client.get_messages(message.chat.id, message.reply_to_message.id)
            file = media.reply_to_message.document or media.reply_to_message.video or media.reply_to_message.audio
            filename = file.file_name
            types = file.mime_type.split("/")
            mime = types[0]
            mg_id = media.reply_to_message.id
            try:
                out = new_name.split(".")
                out[1]
                out_name = out[-1]
                out_filename = new_name
                await message.reply_to_message.delete()
                if mime == "video":
                    markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="doc"),
                            InlineKeyboardButton("🎥 ᴠɪᴅᴇᴏ", callback_data="vid")
                        ]   
                    ]
                )
                elif mime == "audio":
                    markup = InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="doc"), 
                                InlineKeyboardButton("🎵 ᴀᴜᴅɪᴏ", callback_data="aud")
                            ]
                        ]
                    )
                else:
                    markup = InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="doc")
                            ]
                        ]
                    )
                await message.reply_text(
                    text=script.SELECT_FILETYPE_TEXT.format(out_filename),
                    reply_to_message_id=mg_id, 
                    reply_markup=markup
                )

            except:
                try:
                    out = filename.split(".")
                    out_name = out[-1]
                    out_filename = new_name + "." + out_name
                    print(f"out name: {out_filename}")
                except:
                    await message.reply_to_message.delete()
                    await message.reply_text("**ᴇʀʀᴏʀ** : ɴᴏ ᴇxᴛᴇɴꜱɪᴏɴ ɪɴ ꜰɪʟᴇ, ɴᴏᴛ ꜱᴜᴘᴘᴏʀᴛɪɴɢ", reply_to_message_id=mg_id)
                    return
                await message.reply_to_message.delete()
                if mime == "video":
                    markup = InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="doc"), 
                                InlineKeyboardButton("🎥 ᴠɪᴅᴇᴏ", callback_data="vid")
                            ]
                        ]
                    )
                elif mime == "audio":
                    markup = InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="doc"), 
                                InlineKeyboardButton("🎵 ᴀᴜᴅɪᴏ", callback_data="aud")
                            ]
                        ]
                    )
                else:
                    markup = InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="doc")
                            ]
                        ]
                    )
                await message.reply_text(
                    text=script.SELECT_FILETYPE_TEXT.format(out_filename),
                    reply_to_message_id=mg_id, 
                    reply_markup=markup
                )
    except Exception as e:
        print(f"error: {e}")


async def defoultfunc(message):
    try:
        new_name = message
        await message.delete()
        media = await client.get_messages(message.chat.id, message.reply_to_message.id)
        file = media.reply_to_message.document or media.reply_to_message.video or media.reply_to_message.audio
        filename = file.file_name
        types = file.mime_type.split("/")
        mime = types[0]
        mg_id = media.reply_to_message.id
        try:
            out = new_name.split(".")
            out[1]
            out_name = out[-1]
            out_filename = new_name
            await message.reply_to_message.delete()
            if mime == "video":
                markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="doc"),
                        InlineKeyboardButton("🎥 ᴠɪᴅᴇᴏ", callback_data="vid")
                    ]   
                ]
            )
            elif mime == "audio":
                markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="doc"), 
                            InlineKeyboardButton("🎵 ᴀᴜᴅɪᴏ", callback_data="aud")
                        ]
                    ]
                )
            else:
                markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="doc")
                        ]
                    ]
                )
            await message.reply_text(
                text=script.SELECT_FILETYPE_TEXT.format(out_filename),
                reply_to_message_id=mg_id, 
                reply_markup=markup
            )
        
        except:
            try:
                out = filename.split(".")
                out_name = out[-1]
                out_filename = new_name + "." + out_name
                print(f"out name: {out_filename}")
            except:
                await message.reply_to_message.delete()
                await message.reply_text("**ᴇʀʀᴏʀ** : ɴᴏ ᴇxᴛᴇɴꜱɪᴏɴ ɪɴ ꜰɪʟᴇ, ɴᴏᴛ ꜱᴜᴘᴘᴏʀᴛɪɴɢ", reply_to_message_id=mg_id)
                return
            await message.reply_to_message.delete()
            if mime == "video":
                markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="doc"), 
                            InlineKeyboardButton("🎥 ᴠɪᴅᴇᴏ", callback_data="vid")
                        ]
                    ]
                )
            elif mime == "audio":
                markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="doc"), 
                            InlineKeyboardButton("🎵 ᴀᴜᴅɪᴏ", callback_data="aud")
                        ]
                    ]
                )
            else:
                markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="doc")
                        ]
                    ]
                )
            await message.reply_text(
                text=script.SELECT_FILETYPE_TEXT.format(out_filename),
                reply_to_message_id=mg_id, 
                reply_markup=markup
            )
    except Exception as e:
        print(f"error: {e}")
