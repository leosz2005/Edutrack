from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas import payment as payment_schema
from app.crud import payment as payment_crud
from app.db.session import get_db

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/", response_model=payment_schema.PaymentOut)
def create_payment(
    payment_in: payment_schema.PaymentCreate,
    db: Session = Depends(get_db),
):
    """
    Create a new payment in the database.

    Args:
        payment_in (payment_schema.PaymentCreate): The new payment to be created.

    Returns:
        payment_schema.PaymentOut: The newly created payment.
    """
    return payment_crud.create_payment(db=db, payment=payment_in)

@router.get("/", response_model=List[payment_schema.PaymentOut])
def read_payments(db: Session = Depends(get_db)):
    """
    Retrieve a list of all payments in the database.

    Returns:
        List[payment_schema.PaymentOut]: A list of PaymentOut objects.
    """
    return payment_crud.get_payments(db=db)

@router.get("/{payment_id}", response_model=payment_schema.PaymentOut)
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

@router.put("/{payment_id}", response_model=payment_schema.PaymentOut)
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
