from aiogram import Router, F
from aiogram.types import Message
from keyboards.inline import check_subscribe_keyboard
from config import CHANNEL_ID
from aiogram.utils.chat_member import check_is_member

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    user_id = message.from_user.id
    if not await check_is_member(user_id, CHANNEL_ID, message.bot):
        await message.answer("⛔ Botdan foydalanish uchun kanalga obuna bo‘ling:", 
                             reply_markup=check_subscribe_keyboard())
        return
    await message.answer("👋 Salom! Manga botga xush kelibsiz!\n\n📚 /manga — Mangalarni ko‘rish\n➕ /add — Manga qo‘shish")
