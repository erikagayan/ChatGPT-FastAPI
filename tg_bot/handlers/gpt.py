"""
Handler for the /gpt command.
Interacts with GPT-4o to process user requests.
"""

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from tg_bot.utils.gpt import chat_with_gpt
from aiogram.fsm.state import State, StatesGroup

router = Router()

class GPTStates(StatesGroup):
    waiting_for_prompt = State()

@router.message(Command("gpt"))
async def gpt_handler(message: types.Message, state: FSMContext):
    """
    Handle the /gpt command.
    Prompts the user to enter a request for GPT-4o.
    """
    await message.answer("Введите запрос для GPT-4o:")
    # Set the state of waiting for the request input
    await state.set_state(GPTStates.waiting_for_prompt)

@router.message(GPTStates.waiting_for_prompt)
async def process_gpt_prompt(message: types.Message, state: FSMContext):
    """
    Process the user's prompt and send it to GPT-4o.
    """
    prompt = message.text
    response = await chat_with_gpt(prompt)  # # Sending a request to GPT-4o
    if response:  # Sending a response to the user
        await message.answer(response)
    else:
        await message.answer("An error occurred while processing your request.")

    await state.clear()
