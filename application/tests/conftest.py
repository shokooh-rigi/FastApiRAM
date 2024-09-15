# application/tests/conftest.py
import pytest
from sqlalchemy import create_engine

from application.models.ram_model import Base
from databases.session import SessionLocal


@pytest.fixture(scope='function')
def db_session():
    engine = create_engine("sqlite:///:memory:", echo=False)
    SessionLocal.configure(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)
