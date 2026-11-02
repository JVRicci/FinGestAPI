from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    APP_NAME: str
    ENVIROMENT: str

    DATABASE_URL: str
    REDIS_URL: str

    SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        """Configuration for the settings."""

        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
