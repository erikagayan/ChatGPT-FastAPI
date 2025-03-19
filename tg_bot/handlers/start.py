"""
Handle /start command, register user in the database, and show model selection buttons.
"""

import aiohttp
from aiogram import types
from aiogram.filters import Command
from tg_bot.handlers import router
from tg_bot.config import BACKEND_URL
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_keyboard(buttons: list[str], one_time: bool = False) -> ReplyKeyboardMarkup:
    """Creates a dynamic keyboard from a list of button texts."""
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=btn)] for btn in buttons],
        resize_keyboard=True,
        one_time_keyboard=one_time
    )


MODEL_RESPONSES = {
    "ChatGPT": "✅ You have selected ChatGPT. Submit your request.",
    "Anthropic": "✅ This is Anthropic (logic not implemented yet)."
}


@router.message(Command("start"))
async def start_handler(message: types.Message):
    """Handle /start command, register user, and show model selection buttons"""
    user_data = {
        "telegram_id": message.from_user.id,
        "username": message.from_user.username,
        "full_name": message.from_user.full_name
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(f"{BACKEND_URL}/api/users/", json=user_data) as response:
            user = await response.json() if response.status in {200, 201} else None

    if user:
        name = user.get("full_name") or user.get("username") or "User"
        greeting = f"✅ Welcome, {name}!\nYour ID: {user['id']}"
    else:
        greeting = "❌ Registration error."
    await message.answer(greeting, reply_markup=create_keyboard(["ChatGPT", "Anthropic"], one_time=True))


@router.message(lambda msg: msg.text in MODEL_RESPONSES)
async def model_handler(message: types.Message):
    """Handles model selection (ChatGPT or Anthropic)"""
    await message.answer(MODEL_RESPONSES[message.text], reply_markup=create_keyboard(["🔙 Назад"]))


@router.message(lambda msg: msg.text == "🔙 Назад")
async def back_to_selection(message: types.Message):
    """Return to model selection"""
    await message.answer("🔄 Выберите модель:", reply_markup=create_keyboard(["ChatGPT", "Anthropic"], one_time=True))
