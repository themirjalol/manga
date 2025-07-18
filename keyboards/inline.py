from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_ID

def check_subscribe_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Obuna bo‘ldim", callback_data="check_sub")],
        [InlineKeyboardButton(text="🔗 Kanal", url=f"https://t.me/{CHANNEL_ID.lstrip('@')}")]
    ])
