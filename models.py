from typing import Optional, List
from pydantic import ConfigDict
from sqlmodel import Field, SQLModel, Relationship


class UsuariosBase(SQLModel):
    nombre_usuario: Optional[str] = Field(min_length=3, max_length=50)
    email: Optional[str] = Field(unique=True)
    telefono: Optional[int] = Field(default=None, index=True)
    mascota: Optional[bool] = Field(default=True)

class MascotaBase(SQLModel):
    nombre_mascota: Optional[str] = Field(min_length=1, max_length=20)
    raza: Optional[str] = Field(min_length=1, max_length=20)

class MascotaSQL(MascotaBase, table=True):
    __tablename__ = "mascotas"
    id: Optional[int] = Field(default=None, primary_key=True)
    model_config = ConfigDict(from_attributes=True)

    usuario: Optional["UsuarioSQL"] = Relationship(back_populates="mascota")

class UsuarioSQL(UsuariosBase, table=True):
    __tablename__ = "usuarios"
    id: Optional[int] = Field(default=None, primary_key=True)
    model_config = ConfigDict(from_attributes=True)

    mascota: List[MascotaSQL] = Relationship(back_populates="usuario")