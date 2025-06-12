from sqlalchemy import Column, Integer, String, Boolean, column
from sqlalchemy.orm import relationship
from database import Base

class Usuarios(Base):
    __tablename__ = "Usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String)
    email = Column(String, unique =True)
    mascota = Column(Boolean, default= True)

class Mascotas(Base):
    __tablename__ = "Mascotas"
    id_mascota = Column(Integer, primary_key=True, index= True)
    nombre_mascota = Column(String)
    Raza = Column(String)