from models import *
from database import Base

class Usuario(Base):
    __tablename__="usuarios"
    id = column (string, primar)