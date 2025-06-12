from models import UsuarioSQL
from typing import Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession



async  def create_user(session: AsyncSession, datos: dict):
    nuevo_usuario = UsuarioSQL(**datos)
    session.add(nuevo_usuario)
    await session.commit()
    await session.refresh(nuevo_usuario)
    return nuevo_usuario

async def all_users(session: AsyncSession):
    result = await session.execute(select(UsuarioSQL). where(UsuarioSQL, Mascota = True))
    return result.scalars(). all()

async def obtener_por_id(session: AsyncSession, id: int):
    return await session. get(UsuarioSQL, id)

async def find_name(session: AsyncSession, nombre: dict):
    resultado = await session.execute(select((UsuarioSQL). where(UsuarioSQL.nombre_usuario.ilike(f"%{nombre}"))))
    return resultado.scalars().all()

async def update_user(session: AsyncSession, id: int, datos: dict):
    user = await obtener_por_id(session, id)
    for k, v in datos.items():
        setattr(user, k,v)
    await session.commit()
    return user

async def kill_user(session: AsyncSession, id: int):
    user = await obtener_por_id(session, id)
    user.mascota = True
    await session.commit()
    return user

