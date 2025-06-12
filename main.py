from fastapi import FastAPI
from typing import List
from pygments.lexer import default
from models import Usuarios
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

Users =[]

@app.get("/usuario", response_model=List[Usuarios])
async def read_Users():
    return Users

@app.post("/create_user", response_model=List[Usuarios])
async  def create_user(session: AsyncSession, datos: dict):
    nuevo_usuario = Usuarios(**datos)
    session.add(nuevo_usuario)
    await session.commit()
    await session.refresh(nuevo_usuario)
    return nuevo_usuario