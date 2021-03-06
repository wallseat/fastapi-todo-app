from fastapi import FastAPI

from .api.router import api_router
from .db import engine
from .models import metadata

app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs")


@app.on_event("startup")
async def startup():
    metadata.bind = engine


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()


app.include_router(api_router, prefix="/api")
