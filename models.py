from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class usuario(Base):
    __tablename__ = "Usuario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, index=True)
    telefono = Column(Integer)
    mascota = Column(Boolean, default=True)
    eliminada = Column(Boolean, default=False)