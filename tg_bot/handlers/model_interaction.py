"""
Handler for model selection and interaction with GPT-4o and Anthropic Claude.
"""

from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from tg_bot.utils.gpt import chat_with_gpt
from tg_bot.handlers.start import StartStates
from aiogram.fsm.state import State, StatesGroup
from tg_bot.utils.anthropic import chat_with_claude
from tg_bot.handlers.keyboards import model_keyboard, back_keyboard

router = Router()

# The bot is either waiting for a request for GPT or for Claude.
class ModelStates(StatesGroup):
    waiting_for_gpt_prompt = State()
    waiting_for_claude_prompt = State()

@router.message(StartStates.choosing_model)
async def process_model_choice(message: types.Message, state: FSMContext):
    """
    Handle the user's model choice and prompt for input.
    """
    choice = message.text
    if choice == "GPT-4o":
        await state.update_data(selected_model="gpt")
        await message.answer("Enter your request for GPT-4o:", reply_markup=back_keyboard)
        await state.set_state(ModelStates.waiting_for_gpt_prompt)
    elif choice == "Anthropic Claude":
        await state.update_data(selected_model="claude")
        await message.answer("Enter your request for Anthropic Claude:", reply_markup=back_keyboard)
        await state.set_state(ModelStates.waiting_for_claude_prompt)
    else:
        await message.answer("Please select a model from those offered:", reply_markup=model_keyboard)

@router.message(ModelStates.waiting_for_gpt_prompt)
async def process_gpt_prompt(message: types.Message, state: FSMContext):
    """
    Process the user's prompt for GPT-4o and continue conversation.
    """
    if message.text == "Back":
        await message.answer("Choose a model for communication:", reply_markup=model_keyboard)
        await state.set_state(StartStates.choosing_model)
        return

    prompt = message.text
    response = await chat_with_gpt(prompt)
    await message.answer(response, reply_markup=back_keyboard)

@router.message(ModelStates.waiting_for_claude_prompt)
async def process_claude_prompt(message: types.Message, state: FSMContext):
    """
    Process the user's prompt for Anthropic Claude and continue conversation.
    """
    if message.text == "Back":
        await message.answer("Choose a model for communication:", reply_markup=model_keyboard)
        await state.set_state(StartStates.choosing_model)
        return

    prompt = message.text
    response = await chat_with_claude(prompt)
    await message.answer(response, reply_markup=back_keyboard)

@router.message(lambda message: message.text in ["GPT-4o", "Anthropic Claude"])
async def switch_model(message: types.Message, state: FSMContext):
    """
    Handle switching models during conversation.
    """
    choice = message.text
    if choice == "GPT-4o":
        await state.update_data(selected_model="gpt")
        await message.answer("Вы переключились на GPT-4o. Введите запрос:", reply_markup=back_keyboard)
        await state.set_state(ModelStates.waiting_for_gpt_prompt)
    elif choice == "Anthropic Claude":
        await state.update_data(selected_model="claude")
        await message.answer("Вы переключились на Anthropic Claude. Введите запрос:", reply_markup=back_keyboard)
        await state.set_state(ModelStates.waiting_for_claude_prompt)