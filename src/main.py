from fastapi import FastAPI

# from app.api.v1.router import api_router

app = FastAPI(
    title="FastAPI Template",
    description="A template for building FastAPI applications.",
    version="0.1.0",
)

import uvicorn


def dev():
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)


# app.include_router(api_router, prefix="/api/v1")


@app.get("/health-check")
def health_check():
    return {"status": "OK"}
