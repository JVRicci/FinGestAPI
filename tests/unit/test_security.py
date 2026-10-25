from passlib.context import CryptContext

from src.core.security import hash_password, password_context, verify_password


def test_hash_and_verify_long_password():
    password = "a" * 100

    password_hash = hash_password(password)

    assert password_context.identify(password_hash) == "bcrypt_sha256"
    assert password_hash != password
    assert verify_password(password, password_hash)
    assert not verify_password(f"{password}different", password_hash)


def test_verify_legacy_bcrypt_hash():
    password = "correct-horse-battery"
    legacy_hash = CryptContext(schemes=["bcrypt"]).hash(password)

    assert verify_password(password, legacy_hash)
    assert not verify_password(f"{password}extra", legacy_hash)


def test_legacy_bcrypt_rejects_passwords_over_72_bytes():
    legacy_hash = CryptContext(schemes=["bcrypt"]).hash("a" * 72)

    assert not verify_password("a" * 73, legacy_hash)
