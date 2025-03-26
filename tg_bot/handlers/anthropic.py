from aiogram import Router, types
from tg_bot.states import ClaudeStates
from aiogram.fsm.context import FSMContext
from tg_bot.handlers.start import StartStates
from tg_bot.utils.anthropic import chat_with_claude
from tg_bot.handlers.keyboards import model_keyboard, back_keyboard


router = Router()

@router.message(ClaudeStates.waiting_for_prompt)
async def process_claude_prompt(message: types.Message, state: FSMContext):
    if message.text == "Back":
        await message.answer("Choose a model for communication:", reply_markup=model_keyboard)
        await state.set_state(StartStates.choosing_model)
        return

    prompt = message.text
    response = await chat_with_claude(prompt)
    await message.answer(response or "Error accessing Claude.", reply_markup=back_keyboard)
