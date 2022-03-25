from fastapi import APIRouter

from .endpoints import label, todo

api_router = APIRouter()

api_router.include_router(todo.router, prefix="/todo")
api_router.include_router(label.router, prefix="/label")
