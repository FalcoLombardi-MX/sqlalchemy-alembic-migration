from sqlalchemy import Column, String, Integer

from models.base import Base

class RootCause(Base):
    __tablename__ = 'root_cause'
    id = Column(Integer, primary_key=True)
    name = Column(String)