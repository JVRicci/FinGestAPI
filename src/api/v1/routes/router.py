from fastapi import APIRouter

from src.api.v1.routes import transactions_routes, user_routes

api_router = APIRouter()

api_router.include_router(transactions_routes.router)
api_router.include_router(user_routes.router)
