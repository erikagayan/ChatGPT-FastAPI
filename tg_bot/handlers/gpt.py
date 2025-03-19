from aiogram import types
from tg_bot.handlers import router
from tg_bot.utils.gpt import chat_with_gpt


@router.message()
async def gpt_handler(message: types.Message):
    """Processes only messages after ChatGPT selection"""
    if message.text in ["ChatGPT", "Anthropic"]:
        return

    await message.answer("⌛ Think...")
    response = await chat_with_gpt(message.text)
    await message.answer(response)
