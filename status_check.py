# this repo is just a kang of TeleTips With Some Codes And Attributes edit
import os
import re
import pytz
import asyncio
import datetime

from pyrogram import Client, filters
from pyrogram.errors import FloodWait


app = Client(
    name = "Xavier_Bots",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)

TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]
GRP_ID = os.environ.get("GRP_ID")
CHANNEL_NAME = os.environ.get("CHANNEL_NAME", "@Xavier_Bots")

async def main_aakashchecker():
    async with app:
            while True:
                print("Checking...")
                statz = f"<u>**🏷 Welcome To {CHANNEL_NAME} My Updates Channel**</u>\n\n 📈 | <u>**Real Time Bot Stats**</u>"
                for bot in BOT_LIST:
                    await asyncio.sleep(7)
                    try:
                        bot_info = await app.get_users(bot)
                    except Exception:
                        bot_info = bot

                    try:
                        statzz = await app.send_message(bot, "/start")
                        aaa = statzz.id
                        await asyncio.sleep(15)
                        zzz_stats = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_stats:
                            bbb = ccc.id
                        if aaa == bbb:
                            statz += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **Status: Offline ❄**"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(GRP_ID), f"**Bot Is currently Off\n[{bot_info.first_name}](tg://user?id={bot_info.id}) Starting Soon..**")
                                except Exception:...
                            await app.read_chat_history(bot)
                        else:
                            statz += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **Status Online ✨**"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        ttm = re.findall("\d{0,5}", str(e))
                        await asyncio.sleep(int(ttm))
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                statz += f"\n\n✔️ <u>Last Checked On:</u>\n**Date And time: {last_update}**\n**Time Zone: ({TIME_ZONE})**\n\n<i><u>♻️Refreshes In 10 Minutes Automatically.</u></i>\n\n<i>**๏ Powered By @Xavier_Bots ๏**</i>"
                await app.edit_message_text(int(CHANNEL_ID), MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(600)
                        
app.run(main_aakashchecker())
