from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.engine import SessionLocal
from backend.crud import get_users, get_user_by_telegram_id, create_user
from backend.schemas import UserCreate, UserResponse

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/users/", response_model=UserResponse)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await get_user_by_telegram_id(db, user.telegram_id)
    if existing_user:
        return existing_user
    return await create_user(db, user)

@router.get("/users/", response_model=list[UserResponse])
async def read_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await get_users(db, skip, limit)
