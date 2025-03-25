from aiogram import Router, types
from tg_bot.states import GPTStates
from aiogram.fsm.context import FSMContext
from tg_bot.utils.gpt import chat_with_gpt
from tg_bot.handlers.start import StartStates
from tg_bot.handlers.keyboards import model_keyboard, back_keyboard


router = Router()

@router.message(GPTStates.waiting_for_prompt)
async def process_gpt_prompt(message: types.Message, state: FSMContext):
    if message.text == "Back":
        await message.answer("Choose a model for communication:", reply_markup=model_keyboard)
        await state.set_state(StartStates.choosing_model)
        return

    prompt = message.text
    response = await chat_with_gpt(prompt)
    await message.answer(response or "Error accessing GPT.", reply_markup=back_keyboard)
