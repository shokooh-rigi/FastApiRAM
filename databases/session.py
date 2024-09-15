from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from config.settings import settings

# Use SQLite-specific configuration
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Create a new base class for models
Base = declarative_base()
# Create the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Required for SQLite to work with multiple threads
)

# Create a session maker
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def get_db() -> Generator[Session, None, None]:
    try:
        db = SessionLocal()

        yield db  # Yields the session as a dependency
    finally:
        db.close()  # Always close the session after usage


def get_bulk_session() -> Session:
    return SessionLocal()
