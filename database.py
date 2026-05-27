from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Base de datos local en un archivo SQLite
DATABASE_URL = "sqlite:///./mapa_conocimiento.db"

# Configuramos el engine sin pool_size ni max_overflow para evitar errores en SQLite
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}, # Vital para que FastAPI no choque con los hilos de SQLite
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencia para la inyección de sesiones en FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()