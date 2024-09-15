from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from databases.session import Base


class RAMInfo(Base):
    """
    SQLAlchemy model representing RAM information.
    Stores total, free, used memory, and timestamp of the record.
    """
    __tablename__ = 'ram_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    total = Column(Float, nullable=False)
    free = Column(Float, nullable=False)
    used = Column(Float, nullable=False)
    timestamp = Column(DateTime, server_default=func.now())

    @staticmethod
    def create_ram_info(
            db: Session,
            total: float,
            free: float,
            used: float,
            timestamp,
    ):
        """
        Saves a new RAMInfo record to the databases.
        :param db: Database session.
        :param total: Total RAM.
        :param free: Free RAM.
        :param used: Used RAM.
        :param timestamp: Timestamp of the record.
        :return: Saved RAMInfo record.
        """
        ram_info = RAMInfo(
            total=total,
            free=free,
            used=used,
            timestamp=timestamp,
        )
        db.add(ram_info)
        db.commit()
        db.refresh(ram_info)
        return ram_info

    @staticmethod
    def get_last_n_records(db: Session, n: int):
        """
        Retrieves the last n records of RAM info from the databases.
        :param db: Database session.
        :param n: Number of records to retrieve.
        :return: List of RAMInfo records.
        """
        return db.query(
            RAMInfo
        ).order_by(
            RAMInfo.id.desc()
        ).limit(n).all()
