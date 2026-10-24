from sqlalchemy.orm import Session

from src.models.users import User
from src.schemas.user import UserCreate

from src.core.security import hash_password


class UserRepository:
    def __init__(self, db: Session):
        self._db = db

    def create(self, data: UserCreate) -> User:
        user_data = data.model_dump()
        user_data["password"] = hash_password(user_data["password"])

        user = User(**user_data)

        with self._db.begin():
            self._db.add(user)
            self._db.refresh(user)

            return user
