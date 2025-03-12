from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://admin:admin@localhost:5432/chatgpt_bot"

# Creates an engine that manages connections to the database.
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Factory for creating sessions
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

# Creates a base class for all ORM models.
Base = declarative_base()
