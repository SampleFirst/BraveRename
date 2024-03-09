import os
import asyncio
from pyrogram import Client, idle
from plugins.cb_data import app as Client2

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6483924561:AAGgvHt6ocAShXHah-FQV6IXJ7cxps9WDrA")
API_ID = int(os.environ.get("API_ID", "10956858"))
API_HASH = os.environ.get("API_HASH", "cceefd3382b44d4d85be2d83201102b7")
STRING = os.environ.get("STRING", "BQCnMDoATgm6EV5D0XezMULX5ROFq3EMWEf50Sf3AXg8Dhp1s7VoLwDwqNQYIXgj3xtZUmEw7CNh5VFY0h_vBbPuZsMtIuIkLtPIWiGwdvHOJTwhJY-QrEq2297_yz1WvA6HiTvkgwvJtgfqnYBMwf5-rAMjLp6rfG8czJENj0HjRp1wCMpIRrVMyRWw5HElSGzolRUj-LAm3KO38zKa2_xxbovIRaRX5UMSPOJ9HJHphXJ5WZHuWIbfEH1Zufb29-bj0FNwo_2cOSAJWfkhMOJKElujJmXepFsRYBK01JEKKUV-aFWqBwEv-H_pyRpWlS8Mjm897KZhZoE5T5FuATHQ6GoSYwAAAAGCeNZRAQ")


bot = Client(
           "Renamer",
           bot_token=BOT_TOKEN,
           api_id=API_ID,
           api_hash=API_HASH,
           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
