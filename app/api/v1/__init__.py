from fastapi import APIRouter
from app.api.v1.routes import classes, payments, students  # Importa aquí todas tus rutas

api_router = APIRouter()

api_router.include_router(classes.router, prefix="/classes", tags=["Classes"])
api_router.include_router(payments.router, prefix="/payments", tags=["Payments"])
api_router.include_router(students.router, prefix="/students", tags=["Students"])