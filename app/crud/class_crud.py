from sqlalchemy.orm import Session
from app.db.models.class_model import Class
from app.schemas.class_schema import ClassCreate


def create_class(db: Session, class_data: ClassCreate):
    db_class = Class(**class_data.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class


def get_class(db: Session, class_id: int):
    return db.query(Class).filter(Class.id == class_id).first()


def get_classes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Class).offset(skip).limit(limit).all()


def delete_class(db: Session, class_id: int):
    db_class = get_class(db, class_id)
    if db_class:
        db.delete(db_class)
        db.commit()
    return db_class