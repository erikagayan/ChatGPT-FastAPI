"""
Handler for the /anthropic command.
Interacts with Anthropic Claude to process user requests.
"""

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from tg_bot.utils.anthropic import chat_with_claude

router = Router()

class AnthropicStates(StatesGroup):
    waiting_for_prompt = State()

@router.message(Command("anthropic"))
async def anthropic_handler(message: types.Message, state: FSMContext):
    """
    Handle the /anthropic command.
    Prompts the user to enter a request for Anthropic Claude.
    """
    await message.answer("Введите запрос для Anthropic Claude:")
    await state.set_state(AnthropicStates.waiting_for_prompt)

@router.message(AnthropicStates.waiting_for_prompt)
async def process_anthropic_prompt(message: types.Message, state: FSMContext):
    """
    Process the user's prompt and send it to Anthropic Claude.
    """
    prompt = message.text
    response = await chat_with_claude(prompt)
    await message.answer(response)
    await state.clear()
