from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager

from starlette.responses import RedirectResponse

from db_connection import init_db
from routers.parcial import web as parcial

@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_db()
    yield

app = FastAPI(
    title="Parcial",
    description="Parcial",
    version="1.0",
    lifespan=lifespan)

app.mount("/images", StaticFiles(directory="images"), name="images")

templates = Jinja2Templates(directory="templates")

app.include_router(parcial.router, tags=["WEB"], prefix="/web")

@app.get("/", include_in_schema=False)
async def home():
    return RedirectResponse(url="/web/")