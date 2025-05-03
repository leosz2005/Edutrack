from pydantic import BaseModel, EmailStr

class TeacherBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    subject: str | None = None

class TeacherCreate(TeacherBase):
    pass

class TeacherOut(TeacherBase):
    id: int

    class Config:
        from_attributes = True