from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.models import User
from schemas import UserCreate


async def create_user(db: AsyncSession, user: UserCreate) -> User:
    """Create a new user in the database"""
    db_user = User(**user.model_dump())
    db.add(db_user)
    await db.commit()
    return db_user

async def get_user_by_telegram_id(db: AsyncSession, telegram_id: int) -> User | None:
    """Get user by telegram_id"""
    return (await db.execute(select(User).filter_by(telegram_id=telegram_id))).scalar_one_or_none()

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 10) -> list[User]:
    """Get a paginated list of users"""
    return list((await db.execute(select(User).offset(skip).limit(limit))).scalars().all())
