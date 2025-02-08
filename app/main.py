from typing import Optional
from fastapi import FastAPI, Header, HTTPException, Depends, Request
import os
from .models import APICall
from sqlalchemy.orm import Session
from .schemas import NationalIDResposne
from .db import get_db, create_tables
from .utils import EgyptianNationalIDUtility
from slowapi import Limiter
from slowapi.middleware import SlowAPIMiddleware


# create the database tables 
create_tables()


# =================
# 🚀 FASTAPI APP 🚀
# =================

# number of requests per minute 
REQUESTS_PER_MINUTE = 5

# Create the FastAPI application instance.
app = FastAPI()

# Set up the rate limiter
limiter = Limiter(key_func=lambda: None)  # Placeholder

# API keys dictionary
API_KEYS = {
    os.getenv("SERVICE_1"): "SERVICE_1",
    os.getenv("SERVICE_2"): "SERVICE_2",
    os.getenv("NEW_SERVICE") : "NEW_SERVICE"
}


# function to use the api_key as a key for the limiter
def get_api_key(request: Request):
    api_key = request.headers.get("X-API-KEY")
    if api_key not in API_KEYS:
        raise HTTPException(status_code=400, detail="Invalid API KEY.")
    return API_KEYS[api_key]


# Set up the rate limiter
limiter = Limiter(key_func=get_api_key) 
app.state.limiter = limiter 
app.add_middleware(SlowAPIMiddleware)



@app.get(
        "/validate-id",
        response_model=NationalIDResposne
         )
@limiter.limit(f"{REQUESTS_PER_MINUTE}/minute")
async def validate_id(
            request: Request,
            national_id: Optional[str] = None,
            x_api_key: str = Header(...),
            db: Session = Depends(get_db)):
    
    extracted_data = EgyptianNationalIDUtility.validate(national_id)
    api_call = APICall(api_key=x_api_key)
    db.add(api_call)
    db.commit()
    return extracted_data



