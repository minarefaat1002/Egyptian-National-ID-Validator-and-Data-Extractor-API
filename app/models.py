from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .db import Base


# ===========================
# 🌐    APICall Model     🌐
# ==========================+

class APICall(Base):

    # The table name in the database
    __tablename__ = "api_calls" 

    # 🆔 PRIMARY KEY 🆔
    id = Column(Integer, primary_key=True, index=True) 

    # 🔑💻 SERVICE 💻🔑
    service_name = Column(String, index=True)
    
    # 🆔 NATIONAL ID 🆔
    national_id = Column(String)

    # 🕒 TIMESTAMP  🕒
    timestamp = Column(DateTime, default=datetime.utcnow)
