import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.core.security import verify_password
from src.db.base import Base
from src.models.users import UserRole
from src.schemas.user import UserCreate, UserUpdate
from src.repositories.user_repository import UserRepository


@pytest.fixture
def session():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as db:
        yield db
    engine.dispose()


# @pytest.mark.skip()
@pytest.mark.parametrize(
    "user_data",
    [
        UserCreate(
            username="testuser",
            email="testuser@example.com",
            password="testpass",
            role="user",
        )
    ],
)
class TestUserRepository:
    def test_create_user(self, session, user_data):
        # Arrange
        # Act
        user_repo = UserRepository(session)
        user = user_repo.create(user_data)

        # Assert
        assert user.id is not None
        assert user.username == "testuser"
        assert user.email == "testuser@example.com"
        assert user.role is UserRole.USER
        assert user.password != user_data.password
        assert verify_password(user_data.password, user.password)

    def test_create_user_duplicate_username(self, session, user_data):

        # Act
        user_repo = UserRepository(session)
        user_repo.create(user_data)

        with pytest.raises(ValueError):
            user_repo.create(user_data)

    def test_find_by_username(self, session, user_data):
        # Act
        user_repo = UserRepository(session)
        user = user_repo.create(user_data)

        # Assert
        found_user = user_repo.find_by_username("testuser")
        assert found_user is not None
        assert found_user.id == user.id
        assert found_user.username == "testuser"

    def test_find_by_username_not_found(self, session, user_data):
        # Arrange
        user_repo = UserRepository(session)

        # Act
        found_user = user_repo.find_by_username("nonexistentuser")

        # Assert
        assert found_user is None

    def test_update_user(self, session, user_data):
        # Arrange
        user_data_to_update = UserUpdate(
            username="user",
            email="user@example.com",
            password="newpassword",
            role=UserRole.USER,
            active=False,
        )

        # Act
        user_repo = UserRepository(session)
        user = user_repo.create(user_data)

        user_updated = user_repo.update(user_data_to_update, user)

        # Assert
        assert user_updated.id is not None
        assert user_updated.username == "user"
        assert user_updated.email == "user@example.com"
        assert user_updated.role is UserRole.USER
        assert user_updated.password != user_data.password
        # assert verify_password(user_data.password, user_updated.password)
