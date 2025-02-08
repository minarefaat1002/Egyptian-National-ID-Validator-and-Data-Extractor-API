from pydantic import BaseModel

class NationalIDResposne(BaseModel):
    """
    Schema for the extracted information from the national ID.
    """
    national_id: str
    birth_date: str
    gender: str
    governorate: str 
    serial_number: str 
    check_digit: str 