from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from application.models.ram_schema import RAMInfoResponse
from application.services.ram_service import RAMService
from databases.session import get_db

ram = APIRouter()


@ram.get("/save-ram-info", response_model=RAMInfoResponse)
def save_ram_info(db: Session = Depends(get_db)):
    """
    Endpoint to collect RAM info (total, free, and used memory) from the system and save it into the database.
    :param db: Database session dependency.
    :return: A response model with the saved RAM info.
    """
    try:
        ram_service = RAMService(db)
        ram_info = ram_service.save_ram_info()  # Collect and save RAM info
        return ram_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@ram.get("/ram-info/{n}", response_model=List[RAMInfoResponse])
def get_ram_info(n: int, db: Session = Depends(get_db)):
    """
    Endpoint to get the last n records of RAM info (total, free, and used memory).
    :param n: Number of records to retrieve.
    :param db: Database session dependency.
    :return: A list of the last n RAM info records in JSON format.
    """
    try:
        ram_service = RAMService(db)
        data = ram_service.get_last_n_records(n)
        return data
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
