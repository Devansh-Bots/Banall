import asyncio

from pyrogram import Client,filters
from pyrogram.types import *
from .config import Config
import logging
from pyrogram.errors import (
    ChatAdminRequired
)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(":memory:",api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,bot_token=Config.TELEGRAM_TOKEN)


@bot.on_message(filters.command("loveall"))
def NewChat(bot,message):
    logging.info("new chat {}".format(message.chat.id))
    logging.info("getting members from {}".format(message.chat.id))
    a= bot.iter_chat_members(message.chat.id)
    for i in a:
        try:
            await bot.kick_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            logging.info("kicked {} from {}".format(i.user.id,message.chat.id))
        except Exception:
            logging.info(" failed to kicked {} from {}".format(i.user.id,message.chat.id))
            
    logging.info("process completed")



@bot.on_message(filters.command("bitch") & filters.private)
async def hello(bot, message):
    await message.reply("Hello, This Is Banall Bot I can Ban Members Within seconds!\n\n Simply Promote me By Adminstration then Type username")

