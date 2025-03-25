"""
Handler for the /start command.
Fetches user info from Telegram and sends it to the backend.
"""

import aiohttp
from aiogram import Router, types
from aiogram.filters import Command
from tg_bot.config import BACKEND_URL
from tg_bot.states import StartStates
from aiogram.fsm.context import FSMContext
from tg_bot.handlers.keyboards import model_keyboard


router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message, state: FSMContext):
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
                        f"You have successfully registered!\n"
                        "Choose a model for communication:",
                        reply_markup=model_keyboard
                    )
                else:
                    await message.answer(
                        f"Hello, {message.from_user.full_name}!\n"
                        f"Error during registration: {response.status}\n"
                        "Choose a model for communication:",
                        reply_markup=model_keyboard
                    )
    except aiohttp.ClientError as e:
        await message.answer(
            f"Hello, {message.from_user.full_name}!\n"
            f"Error connecting to server: {str(e)}\n"
            "Choose a model for communication:",
            reply_markup=model_keyboard
        )

    await state.set_state(StartStates.choosing_model)
