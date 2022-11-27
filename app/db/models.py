from sqlalchemy import Column, Integer, String # DateTime, ForeignKey, Boolean
from ..core.config import Base
    
    
class Accounts(Base):
    __tablename__ = 'accounts'
    
    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    password = Column(String)