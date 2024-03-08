import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["دارك","المبرمج احمد","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9f156f6b93fa41e45d9ef.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[ძᥲᖇƙ | ɦᥲᥴƙᥱᖇ...💛](https://t.me/A7_M3)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @A7_M3 ❫
◉ 𝙸𝙳      : ❪ `5449190469` ❫
◉ 𝙱𝙸𝙾    : ❪#𝖱ꫀᥲ️ᥣᥣ𝗒,!Ꭵ ძ᥆ꪀ'𝗍 ᥴᥲ️𝗋ꫀ#ɪ'َᴍ 𓏺 𝗔 𝗵 𝗠 𝗲 𝗱 𓏺 ¹🦅🇪🇬{ @D2_RK } ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ძᥲᖇƙ | ɦᥲᥴƙᥱᖇ...💛", url=f"https://t.me/A7_M3"), 
                 ],[
                   InlineKeyboardButton(
                        "𝑆𝑂𝑈𝑅𝐶𝐸 𝐷𝐴𝑅𝐾 🖤", url=f"https://t.me/D2_RK"),
                ],

            ]

        ),

    )
