from typing import Literal
from pydantic import BaseModel, EmailStr, Field

from src.models.users import UserRole


class UserCreate(BaseModel):
    """Schema for creating a user."""

    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    role: Literal["admin", "user"] = "user"
    active: bool = Field(default=True)


class UserUpdate(UserCreate):
    """Schema for updating a user."""

    username: str | None = Field(default=None, min_length=3, max_length=50)
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8)
    role: UserRole | None = None
    active: bool | None = None
