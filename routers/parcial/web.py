from typing import Optional

from fastapi import APIRouter, Request, Query, Depends, Form, File, HTTPException, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from sqlmodel import Session, select

from models import Usuarios, Mascota
from db_connection import get_session
import fuck as crud

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.get("/all_users", response_class=HTMLResponse)
async def get_users(request: Request, session: Session):
    usuarios = await crud.all_users(session)
    return templates.TemplateResponse("usuarios/find.html", {"request": request, "usuarios": usuarios})


@router.get("/new_user", response_class=HTMLResponse)
async def add_user(request: Request):
    return templates.TemplateResponse("usuarios/create.html", {"request": request})

@router.get("/new_user", response_class=HTMLResponse)
async def add_user_process(
        request: Request,
        nombre_usuario:Optional[str] = Form(...),
        email:Optional[str] =Form(None),
        telefono:Optional[int] = Form(None),
        mascota:Optional[bool] = Form(default=False),
        session: Session = Depends(get_session)
):
    user_data = Usuarios (
        nombre_usuario = nombre_usuario,
        email = email,
        telefono = telefono,
        mascota = mascota
    )


    usuario = await crud.create_user(session, user_data)

    session.add(usuario)
    return RedirectResponse("/web/all_users", status_code=303)


@router.get("/update_user", response_class=HTMLResponse)
async def modify_user(request: Request):
    return templates.TemplateResponse("usuarios/update.html", {"request": request})


@router.post("/update_user", response_class=HTMLResponse)
async def modify_user_process(
        request: Request,
        id: Optional[int] = Form(None),
        nombre_usuario:Optional[str] = Form(...),
        email:Optional[str] =Form(None),
        telefono:Optional[int] = Form(None),
        mascota:Optional[bool] = Form(default=False),
        session: Session = Depends(get_session)
):
    user_data = Usuarios(
        nombre_usuario=nombre_usuario,
        email=email,
        telefono=telefono,
        mascota=mascota
    )

    usuario = await crud.update_user(session, id, user_data)
    session.add(usuario)
    return RedirectResponse("/web/all_users", status_code=303)



@router.get("/delete_user", response_class=HTMLResponse)
async def remove_user_process(request: Request):
    return templates.TemplateResponse("usuarios/delete.html", {"request": request})


@router.post("/delete_user", response_class=HTMLResponse)
async def remove_user(request: Request,
                      id: Optional[int] = Form(...),
                      session: Session = Depends(get_session)):

    await crud.kill_user(session, id)
    return RedirectResponse("/web/all_users", status_code=303)



@router.get("/all_pets", response_class=HTMLResponse)
async def get_pets(request: Request, session: Session):
    usuarios = await crud.all_pets(session)
    return templates.TemplateResponse("mascotas/find.html", {"request": request, "usuarios": usuarios})


@router.get("/new_pets", response_class=HTMLResponse)
async def add_pet(request: Request):
    return templates.TemplateResponse("mascotas/create.html", {"request": request})

@router.get("/new_pets", response_class=HTMLResponse)
async def add_pet_process(
        request: Request,
        nombre_mascota:Optional[str] = Form(...),
        raza:Optional[str] = Form(None),
        session: Session = Depends(get_session)
):

    pet_data = Mascota (
        nombre_mascota = nombre_mascota,
        raza = raza
    )

    mascota = await crud.create_pet(session, pet_data)

    session.add(mascota)
    return RedirectResponse("/web/all_pets", status_code=303)



