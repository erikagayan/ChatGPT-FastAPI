from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    telegram_id: int
    username: str | None = Field(None, max_length=50)
    full_name: str | None = Field(None, max_length=100)

class UserResponse(BaseModel):
    id: int
    telegram_id: int
    username: str | None = None
    full_name: str | None = None

    class Config:
        from_attributes = True
