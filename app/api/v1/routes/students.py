from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.student import Student, StudentCreate
from app.db.session import get_db
from app.crud import student as crud_student
from typing import List

router = APIRouter()

@router.post("/", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student in the database.

    Args:
        student (StudentCreate): The new student to be created.

    Returns:
        Student: The newly created student.
    """
    return crud_student.create_student(db, student)

@router.get("/", response_model=List[Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of students, optionally paginated.

    Args:
        skip (int, optional): Number of records to skip. Defaults to 0.
        limit (int, optional): Maximum number of records to return. Defaults to 100.

    Returns:
        List[Student]: A list of Student objects.
    """
    return crud_student.get_student(db, skip=skip, limit=limit)