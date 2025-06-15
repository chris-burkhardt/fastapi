from fastapi import FastAPI
from app.api import algo

app = FastAPI(
    title="Algorithm Solutions API",
    description="API for running and testing algorithmic problem solutions with performance metrics",
    version="1.0.0"
)

app.include_router(algo.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Algorithm Solutions API",
        "docs": "/docs",
        "redoc": "/redoc"
    }
