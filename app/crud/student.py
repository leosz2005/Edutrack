from sqlalchemy.orm import Session
from app.db.models.student import Student
from app.schemas.student import StudentCreate


def create_student(db: Session, student: StudentCreate):
    """
    Create a new student in the database.

    Args:
        db (Session): The active database session.
        student (StudentCreate): The new student to be created.

    Returns:
        Student: The newly created student.
    """
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of students, optionally paginated.

    Args:
        db (Session): SQLAlchemy session to use for the query.
        skip (int, optional): Number of records to skip. Defaults to 0.
        limit (int, optional): Maximum number of records to return. Defaults to 100.

    Returns:
        List[Student]: A list of Student objects.
    """
    return db.query(Student).offset(skip).limit(limit).all()