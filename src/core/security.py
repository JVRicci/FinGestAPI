from passlib.context import CryptContext

password_context = CryptContext(
    schemes=["bcrypt_sha256", "bcrypt"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    if (
        password_context.identify(password_hash) == "bcrypt"
        and len(password.encode("utf-8")) > 72
    ):
        return False
    return password_context.verify(password, password_hash)
