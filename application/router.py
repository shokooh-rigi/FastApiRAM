from fastapi import APIRouter

from application.handelers.ram_handeler import ram

api_router = APIRouter()
api_router.include_router(ram, tags=["ram"])
