from typing import Optional
from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .schemas import NationalIDResposne
from .db import get_db, create_tables
from .utils import EgyptianNationalIDUtility
# load environment variables from .env file 
load_dotenv()




# create the database tables 
create_tables()


# =================
# 🚀 FASTAPI APP 🚀
# =================

# Create the FastAPI application instance.
app = FastAPI()


@app.get(
        "/validate-id",
        response_model=NationalIDResposne
         )
async def validate_id(national_id: Optional[str] = None, x_api_key: str = Header(...)):
    extracted_data = EgyptianNationalIDUtility.validate(national_id)
    return extracted_data



