from sqlalchemy.orm import Session
from app.db.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate

def create_teacher(db: Session, teacher_data: TeacherCreate):
    """
    Create a new teacher in the database.

    Args:
        db (Session): The active database session.
        teacher_data (TeacherCreate): The new teacher data to be created.

    Returns:
        Teacher: The newly created teacher.
    """

    teacher = Teacher(**teacher_data.dict())
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher

def get_teacher(db: Session, teacher_id: int):
    """
    Retrieve a teacher by ID from the database.

    Args:
        db (Session): The active database session.
        teacher_id (int): The ID of the teacher to retrieve.

    Returns:
        Teacher: The retrieved teacher, or None if no matching teacher was found.
    """
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()

def get_teachers(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of teachers, optionally paginated.

    Args:
        db (Session): The active database session.
        skip (int, optional): Number of records to skip. Defaults to 0.
        limit (int, optional): Maximum number of records to return. Defaults to 100.

    Returns:
        List[Teacher]: A list of Teacher objects.
    """
    
    return db.query(Teacher).offset(skip).limit(limit).all()
