#db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

#=========================================
# 🛠️ DATABASE CONFIGURATION Parameters 🛠️
#=========================================


POOL_SIZE = 10
MAX_OVERFLOW = 20
AUTO_COMMIT = False 
AUTO_FLUSH = False

# Load environment variables 
load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")  # PostgreSQL database URL
DATABASE_URL = "postgresql://postgres:postgres@db:5432/postgres"

#===================================
# 🔧       ENGINE CREATION       🔧
#===================================


# Create the SQLAlcehmy engine to connect to the database
engine = create_engine(DATABASE_URL, pool_size=POOL_SIZE, max_overflow=MAX_OVERFLOW)


#===================================
# 🎭        SESSION MAKER        🎭
# ==================================

# Create a configured "Session" class for database interactions.
SessionLocal = sessionmaker(autocommit=AUTO_COMMIT, autoflush=AUTO_FLUSH, bind=engine)

#  Base class for all SQLAlchemy models. 
Base = declarative_base()

# Function to create all tables defined in the models.py.
def create_tables():
    Base.metadata.create_all(bind=engine)


# ==================================
# 🔄 DATABASE SESSION DEPENDENCY 🔄
# ==================================

# FastAPI dependency to get a database session for each request.
# Automatically closes the session after the request is done.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()