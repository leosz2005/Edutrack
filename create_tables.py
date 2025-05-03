# create_tables.py

from app.db.base import Base
from app.db.session import engine
from app.db.models import class_model, student  # Importa todos los modelos

print("Creando tablas...")
Base.metadata.create_all(bind=engine)
print("¡Tablas creadas con éxito!")
