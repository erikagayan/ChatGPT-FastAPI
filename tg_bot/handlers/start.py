# handlers/start.py
"""
Handler for the /start command.
Fetches user info from Telegram and sends it to the backend.
"""

from aiogram import Router, types
from aiogram.filters import Command
import aiohttp
from tg_bot.config import BACKEND_URL

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    """
    Handle the /start command.
    Collects user data and sends it to the backend API.
    """
    user_data = {
        "telegram_id": message.from_user.id,
        "username": message.from_user.username,
        "full_name": message.from_user.full_name
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{BACKEND_URL}/api/users/", json=user_data) as response:
                if response.status == 200 or response.status == 201:
                    await message.answer(
                        f"Hello, {message.from_user.full_name}!\n"
                        f"Your ID: {message.from_user.id}\n"
                        f"You have successfully registered!"
                    )
                else:
                    await message.answer(
                        f"Hello, {message.from_user.full_name}!\n"
                        f"Error during registration: {response.status}"
                    )
    except aiohttp.ClientError as e:
        await message.answer(
            f"Hello, {message.from_user.full_name}!\n"
            f"Error connecting to server: {str(e)}"
        )
