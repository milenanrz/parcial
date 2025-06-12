from typing import Optional, List

from pydantic import ConfigDict
from sqlmodel import SQLModel, Relationship, Field, create_engine
from uuid import uuid4

class Usuarios(SQLModel, table = True):
    nombre_usuario:str = Field(index=True)
    email:str = Field(unique =True)
    telefono:int = Field(default=None, index=True)
    mascota:str = Field(default= True)

class Mascota(SQLModel, table=True):
    id_mascota:int = Field(primary_key=True, index= True)
    nombre_mascota:str = Field(index = True)
    raza: str = Field(index= True)

    id_usuario: int| None = Field(default=None, foreign_key="usuarios.id")

class Usuario_SQL(Usuarios):
    __tablename__ = "Usuarios"
    id: Optional[int] = Field(primary_key=True, default=None)
    model_config = ConfigDict(from_attributes=True)
    user: List[Mascota] = Relationship(back_populates="Usuario")
