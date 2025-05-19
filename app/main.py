from fastapi import FastAPI
from app.api.v1 import api_router
from app.api.v1.routes import classes, payments, students, teachers

app = FastAPI(title="Edutrack API")

app.include_router(api_router, prefix="/api/v1")
app.include_router(classes.router, prefix="/classes", tags=["Classes"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(teachers.router, prefix="/teachers", tags=["Teachers"])

@app.get("/")
async def root():
    return {"message": "Hello World"}