from aiogram import types
from tg_bot.handlers import router
from tg_bot.utils.gpt import chat_with_gpt


@router.message()
async def gpt_handler(message: types.Message):
    """Processes all text messages and feeds them into GPT-4"""
    await message.answer("⌛ Think...")
    response = await chat_with_gpt(message.text)
    await message.answer(response)
