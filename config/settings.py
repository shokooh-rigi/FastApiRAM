import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import ClassVar

# Load environment variables from .env file
load_dotenv(verbose=True)


class Settings(BaseSettings):
    # base settings
    DEBUG: bool = bool(os.getenv("DEBUG", False))
    CACHE: bool = bool(os.getenv("CACHE", False))
    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # # databases configuration
    # DB_NAME: str = os.getenv("DB_NAME", "ram")
    # DB_USER: str = os.getenv("DB_USER", "shokooh")
    # DB_PASSWORD: str = os.getenv("DB_PASSWORD", "shpassword")
    # DB_HOST: str = os.getenv("DB_HOST", "localhost")
    # DB_PORT: str = os.getenv("DB_PORT", "5432")
    # DB_ENGINE: str = os.getenv("DB_ENGINE", "postgresql")
    #
    # # `DATABASE_URL` is dynamically generated, so it's a `ClassVar`
    # DATABASE_URL: ClassVar[str] = "{db_engine}://{user}:{password}@{host}:{port}/{database}".format(
    #     db_engine=DB_ENGINE,
    #     user=DB_USER,
    #     password=DB_PASSWORD,
    #     host=DB_HOST,
    #     port=DB_PORT,
    #     database=DB_NAME,
    # )
    # Databases configuration
    DATABASE_URL: ClassVar[str] = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    # media directory address
    MEDIA_DIRECTORY: str = "media/"

    class Config:
        env_file = ".env"  # Define the .env file location


# Instantiate the settings object
settings = Settings()
