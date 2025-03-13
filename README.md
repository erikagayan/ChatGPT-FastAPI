# ChatGPT-FastAPI
This telegram bot allows you to talk with chatgpt through telegram


## Files
### Backend part:
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
