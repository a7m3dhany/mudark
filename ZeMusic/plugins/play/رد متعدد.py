import asyncio
from ZeMusic import app 
from strings.filters import command
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


italy = [" معرفش يصحبي "]

@app.on_message(filters.text & filters.regex(r"(^|\W)مين(\W|$)"))
async def Italymusic(client, message):
    if "مين" in message.text:
        response = random.choice(italy)
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس", url="https://t.me/D2_RK")]])
        await message.reply(response, reply_markup=keyboard)

