import factory
from sqlalchemy.orm import sessionmaker
from application.models.ram_model import RAMInfo
from databases.session import engine

# Create a Session instance
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
session = SessionLocal()


class RAMInfoFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = RAMInfo
        sqlalchemy_session = session  # Use a Session instance here

    total = factory.Faker('random_number', digits=4)
    free = factory.Faker('random_number', digits=4)
    used = factory.LazyAttribute(lambda o: o.total - o.free)
    timestamp = factory.Faker('date_time_this_decade')
