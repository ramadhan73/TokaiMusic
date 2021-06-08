# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_sticker("")
    await message.reply_text(
        f"""__Hello!! Aku Adalah__ **{bn}**!!\n__Dikelola Oleh__ @gksukaribett 🇲🇨\n┈──────────────────────┈\n➠ __Invite__ [Assistance](https://t.me/@Assistenrams) __masuk kedalam grup kamu__\n➠ __Untuk info dan update selengkapnya ketuk tombol channel dibawah, Terima kasih! Enjoy!__""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                     InlineKeyboardButton(
                                text="➕️ Tambah Aku Kedalam Group ➕️", url="t.me/Musicallyrams_bot?startgroup=true"),
                ],
                [
                     InlineKeyboardButton(text="🔔 Channel", url=f"https://t.me/calonpenyanyi"),
                     InlineKeyboardButton(text="panduan📜", url=f"https://telegra.ph/Music-Bot-Command-04-15")

"),
                ],
                [
                     InlineKeyboardButton(text="📌Owner📌", url="https://t.me/gksukaribett"),
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""__Rams music telah online, tekan tombol dibawah untuk melihat panduan!!__""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "channel", url="https://t.me/calonpenyanyi"),
                    InlineKeyboardButton(
                        "Panduan 📜", url="https://telegra.ph/Music-Bot-Command-04-15")
                ]
            ]
        )
   )

