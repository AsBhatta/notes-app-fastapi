from fastapi import FastAPI
from .config import settings
from .routes import router

app = FastAPI(title="Notes API", version="0.1.0")
app.include_router(router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "environment": settings.app_env,
        "database": settings.database_url,
    }
