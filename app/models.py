from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class APICall(Base):
    __tablename__ = "api_calls"
    id = Column(Integer, primary_key=True, index=True)
    api_key = Column(String, index=True)
    endpoint = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)