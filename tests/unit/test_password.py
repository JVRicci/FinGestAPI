from src.core.security import hash_password, verify_password


class TestPasswordSecurity:
    def test_hash_and_verify_password(self):
        # Arrange
        password = "testpassword"

        # Act
        hashed_password = hash_password(password)
        is_verified = verify_password(password, hashed_password)

        # Assert
        assert hashed_password != password
        assert is_verified
