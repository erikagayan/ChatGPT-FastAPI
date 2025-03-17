# ChatGPT-FastAPI
This telegram bot allows you to talk with chatgpt through telegram



## Installation:
1. Install python 3.10+
2. git clone `https://github.com/erikagayan/ChatGPT-FastAPI.git`
3. `python -m venv .venv`
4. `pip install -r requirements.txt`
5. `python -m tg_bot.main`



## Files
### Telegram Bot (tg_bot/):
1. **config.py** - file for storing project configuration settings.
2. **bot.py** - this file creates and configures the main objects for the Telegram bot to work.
3. 


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
