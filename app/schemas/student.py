from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class StudentBase(BaseModel):
    full_name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    birthdate: Optional[date] = None
    notes: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True