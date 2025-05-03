from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class ClassStatus(str, Enum):
    scheduled = "scheduled"
    completed = "completed"
    cancelled = "cancelled"


class ClassBase(BaseModel):
    title: str
    description: Optional[str] = None
    datetime: datetime
    duration_minutes: int
    status: Optional[ClassStatus] = ClassStatus.scheduled
    student_id: int


class ClassCreate(ClassBase):
    pass


class ClassInDB(ClassBase):
    id: int

    class Config:
        from_attributes = True