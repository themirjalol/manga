from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

manga_list = []

@router.message(F.text == "/add")
async def add_manga(message: Message):
    await message.answer("📥 Manga nomini yuboring:")
    router.message.register(save_manga_name)

async def save_manga_name(message: Message):
    name = message.text.strip()
    manga_list.append(name)
    await message.answer(f"✅ {name} mangasi qo‘shildi!")

@router.message(F.text == "/manga")
async def show_manga(message: Message):
    if not manga_list:
        await message.answer("📭 Hech qanday manga mavjud emas.")
    else:
        await message.answer("📚 Mangalar:\n" + "\n".join(f"• {m}" for m in manga_list))
