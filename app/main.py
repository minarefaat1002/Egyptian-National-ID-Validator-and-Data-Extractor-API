from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, APICall  # Import the model
from datetime import datetime
# load environment variables from .env file 
load_dotenv()


# DATABASE_URL = os.getenv("DATABASE_URL")  # PostgreSQL database URL
DATABASE_URL = "postgresql://postgres:postgres@db:5432/postgres"
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create the database tables 
Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
