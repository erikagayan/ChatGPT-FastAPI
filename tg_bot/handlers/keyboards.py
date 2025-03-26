"""
handlers/keyboards.py
Centralized keyboard definitions for the Telegram bot.
"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BTN_GPT = "GPT-4o"
BTN_CLAUDE = "Anthropic Claude"
BTN_BACK = "Back"

# Keyboard for selecting models
model_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=BTN_GPT), KeyboardButton(text=BTN_CLAUDE)],
    ],
    resize_keyboard=True,
)

# Keyboard with only a back button
back_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=BTN_BACK)],
    ],
    resize_keyboard=True,
)
