"""
Select model, switch between models.
"""
from aiogram import Router, types
from tg_bot.handlers.gpt import GPTStates
from aiogram.fsm.context import FSMContext
from tg_bot.handlers.start import StartStates
from tg_bot.handlers.anthropic import ClaudeStates
from tg_bot.handlers.keyboards import model_keyboard, back_keyboard


router = Router()

# If you pressed the start button
@router.message(StartStates.choosing_model)
async def process_model_choice(message: types.Message, state: FSMContext):
    choice = message.text
    if choice == "GPT-4o":
        await message.answer("Enter your query for GPT-4o:", reply_markup=back_keyboard)
        await state.set_state(GPTStates.waiting_for_prompt)

    elif choice == "Anthropic Claude":
        await message.answer("Enter your query for Anthropic Claude:", reply_markup=back_keyboard)
        await state.set_state(ClaudeStates.waiting_for_prompt)

    else:
        await message.answer("Please select a model from the list:", reply_markup=model_keyboard)

# If you manually select the model
@router.message(lambda message: message.text in ["GPT-4o", "Anthropic Claude"])
async def switch_model(message: types.Message, state: FSMContext):
    choice = message.text
    if choice == "GPT-4o":
        await message.answer("You have switched to GPT-4o. Enter your query:", reply_markup=back_keyboard)
        await state.set_state(GPTStates.waiting_for_prompt)

    elif choice == "Anthropic Claude":
        await message.answer("You have switched to Anthropic Claude. Enter your query:", reply_markup=back_keyboard)
        await state.set_state(ClaudeStates.waiting_for_prompt)
