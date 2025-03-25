"""
Contains different states of the bot
"""
from aiogram.fsm.state import StatesGroup, State

# States for /start
class StartStates(StatesGroup):
    choosing_model = State()

# States for GPT
class GPTStates(StatesGroup):
    waiting_for_prompt = State()

# States for Claude
class ClaudeStates(StatesGroup):
    waiting_for_prompt = State()
