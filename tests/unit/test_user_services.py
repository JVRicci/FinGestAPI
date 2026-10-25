import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.db.base import Base
from src.schemas.user import UserCreate, UserUpdate
from src.services.user_services import UserRepository


@pytest.fixture
def session():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as db:
        yield db
    engine.dispose()


@pytest.mark.parametrize(
    "user_data",
    [
        UserCreate(
            username="testuser",
            email="testuser@example.com",
            password="testpassword",
            role="user",
        ),
    ],
)
class TestUserServices:
    def test_user_create_with_parametrize(self, session, user_data):
        # Arrange
        user_repo = UserRepository(session)
        # Act
        user = user_repo.create(user_data)

        assert user.id is not None
        assert user.username == user_data.username

    def test_update_a_user(self, session, user_data):
        # Arrange
        user_repo = UserRepository(session)
        user_update_data = UserUpdate(
            username="newusername",
            email="newuseremail@example.com",
            password="newpassword",
            role="user",
        )

        # Act
        user = user_repo.create(user_data)
        user_updated = user_repo.update(user_update_data, user)

        # Assert
        assert user.id == user_updated.id

    def test_delete_a_user(self, session, user_data):
        # Arrange
        user_repo = UserRepository(session)

        # Act
        user = user_repo.create(user_data)
        user_repo.delete(user)

        # Assert
        assert user_repo.find_user_by_id(user.id) is None
