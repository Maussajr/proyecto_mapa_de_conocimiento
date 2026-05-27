from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db
import models, schemas
from typing import List

# Crear tablas automáticamente (Solo para desarrollo, en producción usar Alembic)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mapa de Conocimiento API",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Función auxiliar para detectar la PK dinámicamente
def get_pk_name(model):
    return model.__table__.primary_key.columns.keys()[0]

def generic_crud(router_name: str, model, schema):
    @app.get(f"/{router_name}", tags=[router_name.capitalize()], response_model=List[schema])
    def listar(db: Session = Depends(get_db)):
        return db.query(model).all()

    @app.post(f"/{router_name}", tags=[router_name.capitalize()])
    def crear(data: schema, db: Session = Depends(get_db)):
        try:
            nuevo = model(**data.model_dump())
            db.add(nuevo)
            db.commit()
            db.refresh(nuevo)
            return nuevo
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=f"Error en base de datos: {str(e)}")

    @app.delete(f"/{router_name}/{{id}}", tags=[router_name.capitalize()])
    def eliminar(id: str, db: Session = Depends(get_db)):
        pk = get_pk_name(model)
        db_obj = db.query(model).filter(getattr(model, pk) == id).first()
        if not db_obj:
            raise HTTPException(status_code=404, detail="Registro no encontrado")
        db.delete(db_obj)
        db.commit()
        return {"status": "Eliminado"}

# --- REGISTRO DE ENTIDADES ---
generic_crud("areas-conocimiento", models.AreaConocimiento, schemas.AreaConocimientoBase)
generic_crud("ods", models.ObjetivoDesarrolloSostenible, schemas.ODSBase)
generic_crud("docentes", models.Docente, schemas.DocenteBase)
generic_crud("proyectos", models.Proyecto, schemas.ProyectoBase)
# ... añadir resto de endpoints de la misma forma

@app.get("/")
def read_root():
    return {"status": "API Online", "docs": "/docs"}
