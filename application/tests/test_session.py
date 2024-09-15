from contextlib import contextmanager
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Create an in-memory SQLite engine for testing
from databases.session import Base

engine = create_engine("sqlite:///:memory:", echo=False)

# Create a session maker for testing
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Create all tables in the testing database
Base.metadata.create_all(bind=engine)


@contextmanager
def test_get_db() -> Generator:
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def test_get_bulk_session() -> Session:
    return TestingSessionLocal()
