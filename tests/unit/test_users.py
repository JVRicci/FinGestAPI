from sqlalchemy.orm import Session

from src.schemas.user import UserCreate
from src.repositories.user_repository import UserRepository

session = Session()


def test_create_user():
    # Arrange
    user_data = UserCreate(
        username="testuser",
        email="testuser@example.com",
        password="testpass",
        role="user",
    )

    # Act
    user_repo = UserRepository(session)
    user = user_repo.create(user_data)

    # Assert
    assert user.id is not None
    assert user.username == "testuser"
    assert user.email == "testuser@example.com"
    assert user.role == "user"
