from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.schemas.user import UserCreate, UserResponse, UserUpdate
from src.services.user_services import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db),
):
    """Create a new user."""
    service = UserService(db)
    return service.create_user(data)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db),
):
    """Update an existing user."""
    service = UserService(db)
    user = service.find_user_by_id(user_id)
    if not user:
        raise ValueError("User not found")
    return service.update_user(data, user)


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    """Delete a user."""
    service = UserService(db)
    return service.delete_user(user_id)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    """Get a user by ID."""
    service = UserService(db)
    user = service.find_user_by_id(user_id)
    if not user:
        raise ValueError("User not found")
    return user
