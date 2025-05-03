from datetime import date
from pydantic import BaseModel
from typing import Optional
from app.db.models.payment import PaymentStatus

class PaymentBase(BaseModel):
    amount: float
    payment_date: date
    student_id: int
    status: PaymentStatus = PaymentStatus.PENDING

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    payment_date: Optional[date] = None
    student_id: Optional[int] = None
    status: Optional[PaymentStatus] = None

class PaymentOut(PaymentBase):
    id: int

    class Config:
        from_attributes = True
