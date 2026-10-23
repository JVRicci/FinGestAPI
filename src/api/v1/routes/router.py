from fastapi import APIRouter

from src.api.v1.routes import transactions

api_router = APIRouter()

api_router.include_router(transactions.router)
