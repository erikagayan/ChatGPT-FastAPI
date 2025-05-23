# ChatGPT-FastAPI
This telegram bot allows you to talk with chatgpt through telegram

You can use ChatGPT and when you click on the start button your data will be saved in the database


## Installation:
1. Install python 3.10+
2. git clone `https://github.com/erikagayan/ChatGPT-FastAPI.git`
3. `python -m venv .venv`
4. `pip install -r requirements.txt`
5. `uvicorn backend.main:app --reload` in terminal
6. `python -m tg_bot.main`

### Additional
Create `.env` file in ChatGPTFastAPI folder and write:
- BOT_TOKEN
- OPENAI_API_KEY


## Files
### Telegram Bot (tg_bot/):
1. **config.py** - file for storing project configuration settings.
2. **bot.py** - this file creates and configures the main objects for the Telegram bot to work.
3. **main.py** - launch bot
4. **states.py** - сontains different states of the bot
5. **utils/gpt.py** - this module sends requests to GPT-4o and returns AI-generated responses.
6. **utils/anthropic.py** - this module sends requests to Anthropic Claude and returns AI-generated responses.
7. **handlers/start.py** - handle /start command and register user in the database
8. **handlers/gpt.py** - processes all text messages and feeds them into GPT-4
9. **handlers/keyboard.py** - bot keyboard
10. **handlers/model_interaction.py** - select model, switch between models

### Backend:
1. **database/engine.py** - configures a database connection using SQLAlchemy and asyncpg (an asynchronous driver for PostgreSQL)
   - change `echo` to False in production
   - change `pool_size` and `max_overflow` if there are more users

2. **database/models.py** - models of DB
   - id
   - telegram_id
   - username
   - fullname

3. **schemas.py** - needed to define data schemas using Pydantic. Used to validate API input and output data.
4. **crud.py** - contains asynchronous functions for working with users in the database using SQLAlchemy
