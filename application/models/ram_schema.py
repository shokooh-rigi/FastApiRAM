from pydantic import BaseModel
from datetime import datetime


class RAMInfoResponse(BaseModel):
    """
    Pydantic model representing the RAM info response.
    """
    total: float
    free: float
    used: float
    timestamp: datetime

    class Config:
        from_attributes = True
        orm_mode = True
