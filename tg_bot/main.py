import asyncio
from aiogram import Dispatcher
from bot.bot import *
from handlers import start

async def main():
    dp.include_router(start.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
