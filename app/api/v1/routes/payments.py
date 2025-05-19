from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date

from app.db.models.payment import Payment, PaymentStatus

from app.schemas import payment as payment_schema
from app.crud import payment as payment_crud
from app.db.session import get_db

router = APIRouter(tags=["Payments"])

@router.post("/", response_model=payment_schema.PaymentResponse)
def create_payment(
    payment_in: payment_schema.PaymentCreate,
    db: Session = Depends(get_db),
):
    """
    Create a new payment in the database.

    Args:
        db:
        payment_in (payment_schema.PaymentCreate): The new payment to be created.

    Returns:
        payment_schema.PaymentOut: The newly created payment.
    """
    return payment_crud.create_payment(db=db, payment=payment_in)

@router.get("/", response_model=List[payment_schema.PaymentResponse])
def get_payments(
    db: Session = Depends(get_db),
    status: Optional[PaymentStatus] = Query(None),
    student_id: Optional[int] = Query(None),
    method: Optional[str] = Query(None),
    date_from: Optional[date] = Query(None),
    date_to: Optional[date] = Query(None),
):
    """
    Retrieve a list of payments, optionally filtered by status, student_id, method, and date range.

    Args:
        db (Session): The active database session.
        status (Optional[PaymentStatus]): The status of the payments to retrieve.
        student_id (Optional[int]): The ID of the student to retrieve payments for.
        method (Optional[str]): The payment method used by the payments to retrieve.
        date_from (Optional[date]): The earliest date to retrieve payments for.
        date_to (Optional[date]): The latest date to retrieve payments for.

    Returns:
        List[payment_schema.PaymentResponse]: A list of Payment objects, or an empty list if no matching payments were found.
    """
    query = db.query(Payment)

    if status:
        query = query.filter(Payment.status == status)
    if student_id:
        query = query.filter(Payment.student_id == student_id)
    if method:
        query = query.filter(Payment.method == method)
    if date_from:
        query = query.filter(Payment.created_at >= date_from)
    if date_to:
        query = query.filter(Payment.created_at <= date_to)

    return query.all()

@router.get("/{payment_id}", response_model=payment_schema.PaymentResponse)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a payment by ID from the database.

    Args:
        payment_id (int): The ID of the payment to retrieve.
        db (Session): The active database session.

    Returns:
        payment_schema.PaymentOut: The retrieved payment, or a 404 error if no matching payment was found.
    """

    payment = payment_crud.get_payment(db=db, payment_id=payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.put("/{payment_id}", response_model=payment_schema.PaymentResponse)
def update_payment(
    payment_id: int,
    payment_in: payment_schema.PaymentUpdate,
    db: Session = Depends(get_db),
):
    """
    Update a payment in the database.

    Args:
        payment_id (int): The ID of the payment to update.
        payment_in (payment_schema.PaymentUpdate): The payment data to be updated.

    Returns:
        payment_schema.PaymentOut: The updated payment, or a 404 error if no matching payment was found.
    """
    updated_payment = payment_crud.update_payment(db=db, payment_id=payment_id, payment_update=payment_in)
    if not updated_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return updated_payment

@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    """
    Delete a payment by ID from the database.

    Args:
        payment_id (int): The ID of the payment to delete.
        db (Session): The active database session.

    Returns:
        dict: A dict with a boolean "ok" key and a string "message" key.
    """
    deleted_payment = payment_crud.delete_payment(db=db, payment_id=payment_id)
    if not deleted_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"ok": True, "message": "Payment deleted successfully"}
