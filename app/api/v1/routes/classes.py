from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.class_schema import ClassCreate, ClassInDB
from app.crud import class_crud
from app.db.session import get_db
from typing import List

router = APIRouter()


@router.post("/", response_model=ClassInDB)
def create_class(class_data: ClassCreate, db: Session = Depends(get_db)):
    return class_crud.create_class(db, class_data)


@router.get("/", response_model=List[ClassInDB])
def list_classes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return class_crud.get_classes(db, skip, limit)
