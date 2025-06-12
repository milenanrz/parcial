from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import usuario

async def crear_usuario(session: AsyncSession, datos: dict):
    nueva_usuario = usuario(**datos)
    session.add(nueva_usuario)
    await session.commit()
    await session.refresh(nueva_usuario)
    return nueva_usuario

async def obtener_todas(session: AsyncSession):
    resultado = await session.execute(select(usuario).where(usuario.eliminada == False))
    return resultado.scalars().all()

async def obtener_por_id(session: AsyncSession, id: int):
    return await session.get(usuario, id)

async def buscar_por_nombre(session: AsyncSession, nombre: str):
    resultado = await session.execute(select(usuario).where(usuario.nombre.ilike(f"%{nombre}%")))
    return resultado.scalars().all()

async def editar_usuario(session: AsyncSession, id: int, datos: dict):
    user = await obtener_por_id(session, id)
    for k, v in datos.items():
        setattr(user, k, v)
    await session.commit()
    return user

async def eliminar_usuario(session: AsyncSession, id: int):
    user = await obtener_por_id(session, id)
    user.eliminada = True
    await session.commit()
    return user