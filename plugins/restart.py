import datetime
import random
import time
import os
import requests
from info import *

restart_time_minutes = random.randint(2, 5)
restart_time_seconds = random.randint(0, 59)
restart_time = datetime.timedelta(minutes=restart_time_minutes, seconds=restart_time_seconds)


is_restarted = True

def send_restart_message():
    restart_message = f"⚡ Bot Restarted ⚡\n🥂 Time Taken: {restart_time_minutes} Minutes {restart_time_seconds} Seconds"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": SUPPORT_CHAT,
        "text": restart_message
    }
    response = requests.post(url, json=data)
    if response.status_code != 200:
        print(f"Failed to send restart message. Error: {response.text}")

time.sleep(10)

if is_restarted:
    send_restart_message()
    
