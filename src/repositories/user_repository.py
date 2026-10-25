from sqlalchemy.orm import Session
from sqlalchemy import select

from src.models.users import User, UserRole
from src.schemas.user import UserCreate, UserUpdate

from src.core.security import hash_password


class UserRepository:
    def __init__(self, db: Session):
        self._db = db

    def create(self, data: UserCreate) -> User:
        user_data = data.model_dump()

        with self._db.begin():
            if self.find_by_username(user_data["username"]):
                raise ValueError("Username already exists")

            user_data["password"] = hash_password(user_data["password"])
            user_data["role"] = UserRole(user_data["role"])

            user = User(**user_data)

            self._db.add(user)
            self._db.flush()
            self._db.refresh(user)

            return user

    def find_by_username(self, username: str) -> User | None:
        return self._db.execute(
            select(User).filter_by(username=username)
        ).scalar_one_or_none()

    def update(self, UserUpdate: UserUpdate, user: User) -> User:
        user_data = UserUpdate.model_dump(exclude_unset=True)

        # if user_data.get("role") is not None:
        #     user_data["role"] = UserRole(user_data["role"])

        with self._db.begin():

            stmt = select(User).filter_by(id=user.id).with_for_update()
            user = self._db.execute(stmt).scalar_one()

            if user_data.get("password"):
                user_data["password"] = hash_password(user_data["password"])

            for key, value in user_data.items():
                setattr(user, key, value)

            self._db.add(user)
            self._db.flush()
            self._db.refresh(user)

            return user

    def delete(self, user: User) -> None:
        with self._db.begin():
            self._db.delete(user)
