import uvicorn
from fastapi import FastAPI

from src.api.v1.routes.router import api_router

app = FastAPI(
    title="FastAPI",
    description="API for finances control",
    version="0.1.0",
)

app.include_router(api_router, prefix="/api/v1")


def dev():
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)


@app.get("/health-check")
def health_check():
    return {"status": "OK"}
