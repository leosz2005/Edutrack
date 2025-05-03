from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from app.db.models.payment import PaymentStatus

class PaymentBase(BaseModel):
    amount: float
    created_at: datetime
    student_id: int
    status: PaymentStatus = PaymentStatus.PENDING

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    payment_date: Optional[datetime] = None
    student_id: Optional[int] = None
    status: Optional[PaymentStatus] = None

class PaymentResponse(PaymentBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
