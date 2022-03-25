from fastapi import APIRouter

from .v1.router import api_router as v1_router

api_router = APIRouter()

api_router.include_router(v1_router, prefix="/v1")
