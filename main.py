import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, admin, manga

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(start.router, admin.router, manga.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())