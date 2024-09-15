import logging
from datetime import datetime

import psutil
from sqlalchemy.orm import Session

from application.models.ram_model import RAMInfo
from application.models.ram_schema import RAMInfoResponse

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class RAMService:
    """
    Service class responsible for handling business logic related to RAM information.
    """

    def __init__(self, db: Session):
        """
        Initialize RAMService with a databases session.
        :param db: Database session.
        """
        self.db = db

    def save_ram_info(self) -> RAMInfoResponse:
        """
        Collects RAM information from the system using psutil and saves it to the database.
        :return: RAMInfoResponse containing the saved RAM info.
        """
        try:
            logger.info("Collecting RAM information from the system.")
            ram = psutil.virtual_memory()
            total = ram.total / (1024 ** 2)  # Convert bytes to megabytes
            free = ram.available / (1024 ** 2)
            used = total - free
            logger.info(f"RAM info collected: Total={total}, Free={free}, Used={used}")
            ram_info = RAMInfo.create_ram_info(
                db=self.db,
                total=total,
                free=free,
                used=used,
                timestamp=datetime.now(),
            )
            logger.info("RAM information saved successfully.")
            return RAMInfoResponse(
                total=ram_info.total,
                free=ram_info.free,
                used=ram_info.used,
                timestamp=ram_info.timestamp
            )
        except Exception as e:
            logger.error(f"Error occurred while saving RAM info: {e}")
            raise

    def get_last_n_records(self, n: int):
        """
        Retrieves the last n records of RAM info from the databases.
        :param n: Number of records to retrieve.
        :return: A list of the last n RAMInfo records as RAMInfoResponse objects.
        :raises ValueError: If n is less than or equal to 0 or no data is found.
        """
        logger.info(f"Fetching the last {n} records from the database.")
        if n <= 0:
            logger.error("Invalid parameter: n must be greater than 0.")
            raise ValueError("The parameter n must be greater than 0.")

        # Call the RAMInfo's method to fetch records from the databases
        records = RAMInfo.get_last_n_records(db=self.db, n=n)
        if not records:
            logger.warning("No RAM info records found.")
            raise ValueError("No data found.")

        # Use Pydantic model for response
        return [RAMInfoResponse.from_orm(record) for record in records]
