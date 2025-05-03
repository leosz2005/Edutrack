from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.teacher import TeacherCreate, TeacherOut
from app.crud import teacher as teacher_crud

router = APIRouter(prefix="/teachers", tags=["teachers"])

@router.post("/", response_model=TeacherOut)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """
    Create a new teacher in the database.

    Args:
        teacher (TeacherCreate): The new teacher to be created.

    Returns:
        TeacherOut: The newly created teacher.
    """
    return teacher_crud.create_teacher(db, teacher)

@router.get("/{teacher_id}", response_model=TeacherOut)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a teacher by ID from the database.

    Args:
        teacher_id (int): The ID of the teacher to retrieve.

    Returns:
        TeacherOut: The retrieved teacher, or a 404 error if no matching teacher was found.
    """
    db_teacher = teacher_crud.get_teacher(db, teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher

@router.get("/", response_model=list[TeacherOut])
def read_teachers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of teachers, optionally paginated.

    Args:
        skip (int, optional): Number of records to skip. Defaults to 0.
        limit (int, optional): Maximum number of records to return. Defaults to 100.

    Returns:
        List[TeacherOut]: A list of TeacherOut objects.
    """

    return teacher_crud.get_teachers(db, skip=skip, limit=limit)
