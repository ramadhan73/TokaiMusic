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
    await message.send_sticker("CAACAgIAAxkBAAEKL_1gt842-B5SnR5eHrlBsfTviEt2GwACrAsAAt_YUUnNC_qAE0qWKR8E")
    await message.send_text(
        f"""_Hello!! Aku Adalah_ *{bn}*!!\n_Dikelola Oleh_ @Insaynn 🇲🇨\n┈──────────────────────┈\n
            ➠ _Invite_ [Assistance](https://t.me/TokaiMusicAssistance) _masuk kedalam grup kamu_\n➠ _Untuk info dan update selengkapnya ketuk tombol channel dibawah, Terima kasih! Enjoy!_""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                     InlineKeyboardButton(
                                text="➕️ Tambah Aku Kedalam Group ➕️", url="t.me/TokaiMusicBot?startgroup=true"),
                ],
                [
                     InlineKeyboardButton(text="🔔 Channel", url=f"https://t.me/TokaiProject"),
                     InlineKeyboardButton(text="Group 🔊", url=f"https://t.me/musikalitasID"),
                ],
                [
                     InlineKeyboardButton(text="📱 Instagram 📱", url="https://instagram.com/sndykaa/"),
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""_Tokai Music telah online, ketik_ /help _untuk panduan melihat panduan secara langsung!!_""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🇲🇨 Donate", url="https://t.me/Insaynn"),
                    InlineKeyboardButton(
                        "Panduan 📜", url="https://telegra.ph/Music-Bot-Command-04-15")
                ]
            ]
        )
   )

