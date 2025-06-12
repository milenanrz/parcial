from typing import Optional, List

from pydantic import ConfigDict
from pydantic.v1 import BaseModel
from sqlmodel import SQLModel, Relationship, Field, create_engine
from uuid import uuid4

class Usuarios(SQLModel, table = True):
    id_user:Optional[int] = Field(default=None, primary_key=True)
    nombre_usuario:Optional[str] = Field(index=True)
    email:Optional[str] = Field(unique =True)
    telefono:Optional[int] = Field(default=None, index=True)
    mascota:Optional[bool] = Field(default= True)

class Mascota(SQLModel, table=True):
    id_mascota:Optional[int] = Field(primary_key=True, index= True)
    nombre_mascota:Optional[str] = Field(index = True)
    raza: Optional[str] = Field(index= True)

    id_usuario: Optional[int]| None = Field(default=None, foreign_key="usuarios.id")

class Usuario_SQL(Usuarios):
    __tablename__ = "Usuarios"
    id: Optional[int] = Field(primary_key=True, default=None)
    model_config = ConfigDict(from_attributes=True)
    user: List[Mascota] = Relationship(back_populates="Usuarios")