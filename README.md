# ChatGPT-FastAPI


## Files
**engine.py** - configures a database connection using SQLAlchemy and asyncpg (an asynchronous driver for PostgreSQL)
- change `echo` to False in production
- change `pool_size` and `max_overflow` if there are more users