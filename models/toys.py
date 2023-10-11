from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Toyss(Base):
    
    __tablename__ = "toys"
    
    id = Column(Integer, primary_key = True)
    title = Column(String)
    code = Column(Integer)
    category = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    desciption = Column(String)
    
    