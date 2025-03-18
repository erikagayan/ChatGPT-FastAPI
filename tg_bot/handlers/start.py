"""
Handler that greets the user and displays his full name
"""

from aiogram import types
from tg_bot.handlers import router
from aiogram.filters import Command


@router.message(Command("start"))
async def start_handler(message: types.Message):
    """Handle /start command and send a simple greeting"""
    user_name = message.from_user.full_name
    await message.answer(f"Hello, {user_name}!")
