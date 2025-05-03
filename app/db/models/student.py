from sqlalchemy import Column, Integer, String, Date
from app.db.base_class import Base
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    birthdate = Column(Date, nullable=True)
    notes = Column(String, nullable=True)

    classes = relationship("Class", back_populates="student")
    payments = relationship("Payment", back_populates="student")