from fastapi import FastAPI
from typing import List
from pygments.lexer import default
from models import Usuarios, Mascota
from sqlalchemy.ext.asyncio import AsyncSession
from fuck import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

Users =[]

@app.get("/usuario", response_model=List[Usuarios])
async def read_Users():
    return Users

@app.post("/create_user")
async  def create_user(usuario: Usuarios, session: AsyncSession)->Usuarios:
    session.add(usuario)
    await session.commit()
    await session.refresh(usuario)
    return usuario