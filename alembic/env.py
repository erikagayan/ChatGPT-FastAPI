from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
import sys
import asyncio

sys.path.append(".")

from database.engine import SQLALCHEMY_DATABASE_URL
from database.models import Base

config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def get_engine():
    return create_async_engine(SQLALCHEMY_DATABASE_URL, poolclass=pool.NullPool)

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=SQLALCHEMY_DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    """Run migrations in 'online' mode."""
    engine = get_engine()
    async with engine.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await engine.dispose()

def do_run_migrations(connection):
    """Настройка Alembic"""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
