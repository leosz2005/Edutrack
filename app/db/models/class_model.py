from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.db.base import Base


class ClassStatus(str, enum.Enum):
    scheduled = "scheduled"
    completed = "completed"
    cancelled = "cancelled"


class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    datetime = Column(DateTime, default=datetime.astimezone)
    duration_minutes = Column(Integer, default=60)
    status = Column(Enum(ClassStatus), default=ClassStatus.scheduled)
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="classes")
