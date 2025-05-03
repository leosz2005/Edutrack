import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# --- Cargar .env ---
from dotenv import load_dotenv

# Carga el .env en la raíz del proyecto
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

# --- Agregar la carpeta 'app' al sys.path ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- Importar settings y base de modelos ---
from core.config import settings
from db.base import Base  # <- Asegúrate que este Base importa todos tus modelos

# --- Configuración de Alembic ---
config = context.config

# Interpretar el archivo .ini para configuraciones de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# URL de la base de datos desde tu settings
target_metadata = Base.metadata
DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL

def run_migrations_offline():
    """Correr migraciones en modo 'offline'."""
    url = DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,  # Detecta cambios en tipos de columnas
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Correr migraciones en modo 'online'."""
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = DATABASE_URL

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # Detecta cambios en tipos de columnas
        )

        with context.begin_transaction():
            context.run_migrations()

# Decidir si corremos offline u online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()