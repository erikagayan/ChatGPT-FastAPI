"""
Handle /start command and register user in the database
"""

from aiogram import types
from tg_bot.handlers import router
from aiogram.filters import Command

import aiohttp
from tg_bot.config import BACKEND_URL


@router.message(Command("start"))
async def start_handler(message: types.Message):
    """Handle /start command and register user in the database"""
    user_data = {
        "telegram_id": message.from_user.id,
        "username": message.from_user.username,
        "full_name": message.from_user.full_name
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(f"{BACKEND_URL}/api/users/", json=user_data) as response:
            if response.status in {200, 201}:
                user = await response.json()
                await message.answer(
                    f"✅ Welcome, {user['full_name'] or user['username'] or 'User'}!\nYour ID: {user['id']}")
            else:
                await message.answer("❌ Registration error. Please try again later.")
