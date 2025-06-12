from fastapi import FastAPI, Request, Form, UploadFile, File, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import os

from database import get_session, engine, Base
from crud import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
#app.mount("/imagenes", StaticFiles(directory="imagenes"), name="imagenes")
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/registrar", response_class=HTMLResponse)
async def formulario_registro(request: Request):
    return templates.TemplateResponse("registrar.html", {"request": request})

@app.post("/registrar")
async def registrar(request: Request, nombre: str = Form(...), email:str = Form(...),telefono: int = Form(...), ano: int = Form(...), session: AsyncSession = Depends(get_session)):
#    ruta_imagen = f"imagenes/{imagen.filename}"
  #  with open(ruta_imagen, "wb") as buffer:
 #       shutil.copyfileobj(imagen.file, buffer)
#
    datos = {"nombre":nombre , "email":email,"telefono":telefono , "ano":ano,"eliminada": False}
    await crear_usuario(session, datos)
    return RedirectResponse(url="/registrar", status_code=303)

@app.get("/usuarios", response_class=HTMLResponse)
async def ver_usuarios(request: Request, session: AsyncSession = Depends(get_session)):
    user = await obtener_todas(session)
    return templates.TemplateResponse("lista.html", {"request": request, "user": user})

@app.get("/usuarios/{id}", response_class=HTMLResponse)
async def ver_detalle(request: Request, id: int, session: AsyncSession = Depends(get_session)):
    user = await obtener_por_id(session, id)
    return templates.TemplateResponse("detalle.html", {"request": request, "user": user})

@app.post("/eliminar/{id}")
async def eliminar(id: int, session: AsyncSession = Depends(get_session)):
    await eliminar_usuario(session, id)
    return RedirectResponse(url="/usuarios", status_code=303)