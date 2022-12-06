from sqlalchemy import Boolean, Column, Integer, String, Float, enu
from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, unique = True, index = True)
    price = Column(Float, unique = True, index = True)
    temperature = Column(Integer, index = True)
    category = Column(Integer, index = True)