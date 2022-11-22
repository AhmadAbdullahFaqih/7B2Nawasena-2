from sqlalchemy import Column, Integer, String
from config import Base

class Cars(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key = True)
    brand = Column(String)
    model = Column(String)
    price = Column(String)