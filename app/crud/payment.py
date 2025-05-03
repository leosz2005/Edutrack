from sqlalchemy.orm import Session
from app.db.models.payment import Payment, PaymentStatus
from app.schemas.payment import PaymentCreate, PaymentUpdate

def create_payment(db: Session, payment: PaymentCreate) -> Payment:
    """
    Create a new payment in the database.

    Args:
        db (Session): The active database session.
        payment (PaymentCreate): The payment data to be created.

    Returns:
        Payment: The newly created payment.
    """
    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_payment(db: Session, payment_id: int) -> Payment | None:
    """
    Retrieve a payment by ID from the database.

    Args:
        db (Session): The active database session.
        payment_id (int): The ID of the payment to retrieve.

    Returns:
        Payment | None: The retrieved payment, or None if no matching payment was found.
    """
    return db.query(Payment).filter(Payment.id == payment_id).first()

def get_payments_by_student(db: Session, student_id: int) -> list[Payment]:
    """
    Retrieve all payments for a student.

    Args:
        db (Session): The active database session.
        student_id (int): The ID of the student to retrieve payments for.

    Returns:
        list[Payment]: A list of payments for the student.
    """
    return db.query(Payment).filter(Payment.student_id == student_id).all()

def update_payment(db: Session, payment_id: int, payment_update: PaymentUpdate) -> Payment | None:
    """
    Update an existing payment in the database.

    Args:
        db (Session): The active database session.
        payment_id (int): The ID of the payment to update.
        payment_update (PaymentUpdate): The payment data to be updated.

    Returns:
        Payment | None: The updated payment, or None if no matching payment was found.
    """
    db_payment = get_payment(db, payment_id)
    if not db_payment:
        return None
    for key, value in payment_update.dict(exclude_unset=True).items():
        setattr(db_payment, key, value)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def delete_payment(db: Session, payment_id: int) -> bool:
    """
    Delete a payment from the database by its ID.

    Args:
        db (Session): The active database session.
        payment_id (int): The ID of the payment to delete.

    Returns:
        bool: True if the payment was successfully deleted, False if no matching payment was found.
    """

    
    db_payment = get_payment(db, payment_id)
    if not db_payment:
        return False
    db.delete(db_payment)
    db.commit()
    return True