from sqlalchemy.orm import Session

from src.core.redis import redis_client
from src.repositories.user_repository import UserRepository
from src.schemas.user import UserCreate, UserUpdate


class UserService:
    def __init__(self, db: Session):
        self._repository = UserRepository(db)

    def create_user(self, data: UserCreate):
        """Create a new user

        Args:
            data (UserCreate): Data for creating a new user.
        """
        user = self._repository.create(data)

        redis_client.delete("dashboard:summary")

        return user

    def update_user(self, data: UserUpdate, user):
        """Update an existing user

        Args:
            data (UserUpdate): Data for updating the user.
            user: The user instance to be updated.
        """

        user._updated = self._repository.update(data, user)

        return user

    def delete_user(self, id):
        """Delete an user

        Args:
            id (int): user id
        """
        if self._repository.find_user_by_id(id) is None:
            raise ValueError("Usuário não existe")

        stmt = self._repository.delete(id)

        return stmt

    def find_user_by_id(self, id):
        """Find a user by id

        Args:
            id (int): user id
        """
        user = self._repository.find_user_by_id(id)

        return user

    def find_user_by_username(self, username):
        """Find a user by username

        Args:
            username (str): user username
        """
        user = self._repository.find_user_by_username(username)

        return user
