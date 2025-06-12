from itertools import product

from fastapi import FastAPI, APIRouter

from models import UsuarioSQL
from typing import Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session
#app = FastAPI()

#user_router= APIRouter()
#product_router = APIRouter()


async def create_users(session: Session, usuario:UsuarioSQL):
    db_usuario = UsuarioSQL.model_validate(usuario, from_attributes=True)

    session.add(db_usuario)
    await session.commit()
    await session.refresh(db_usuario)

    return db_usuario


async  def create_user(session: Session, datos: dict):
    nuevo_usuario = UsuarioSQL(**datos)
    session.add(nuevo_usuario)
    await session.commit()
    await session.refresh(nuevo_usuario)
    return nuevo_usuario

async def all_users(session: Session):
    result = await session.execute(select(UsuarioSQL). where(UsuarioSQL, MascotaSQL = True))
    return result.scalars(). all()

async def obtener_por_id(session: Session, id: int):
    return await session. get(UsuarioSQL, id)

async def find_name(session: Session, nombre: dict):
    resultado = await session.execute(select((UsuarioSQL). where(UsuarioSQL.nombre_usuario.ilike(f"%{nombre}"))))
    return resultado.scalars().all()

async def update_user(session: Session, id: int, datos: dict):
    user = await obtener_por_id(session, id)
    for k, v in datos.items():
        setattr(user, k,v)
    await session.commit()
    return user

async def kill_user(session: Session, id: int):
    user = await obtener_por_id(session, id)
    user.mascota = True
    await session.commit()
    return user