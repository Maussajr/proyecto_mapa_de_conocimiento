from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models, schemas
from typing import List


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mapa de conocimiento",
    description="API Completa para la gestión de 21 tablas del Mapa de Conocimiento",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def generic_crud(router_name: str, model, schema):
    @app.get(f"/{router_name}", tags=[router_name.capitalize()], response_model=List[schema])
    def listar(db: Session = Depends(get_db)):
        return db.query(model).all()

    @app.post(f"/{router_name}", tags=[router_name.capitalize()])
    def crear(data: schema, db: Session = Depends(get_db)):
        nuevo = model(**data.model_dump())
        db.add(nuevo); db.commit(); db.refresh(nuevo)
        return nuevo

    @app.delete(f"/{router_name}/{{id}}", tags=[router_name.capitalize()])
    def eliminar(id: int, db: Session = Depends(get_db)):
    
        pk_name = "cedula" if router_name == "docentes" else "id"
        if router_name == "aliados": pk_name = "nit"
        
        db_obj = db.query(model).filter(getattr(model, pk_name) == id).first()
        if not db_obj: raise HTTPException(status_code=404)
        db.delete(db_obj); db.commit()
        return {"status": "Registro eliminado"}

# --- REGISTRO DE TODAS LAS TABLAS ---

# 1-7. Tablas Maestras y Configuración
generic_crud("areas-conocimiento", models.AreaConocimiento, schemas.AreaConocimientoBase)
generic_crud("ods", models.ObjetivoDesarrolloSostenible, schemas.ODSBase)
generic_crud("areas-aplicacion", models.AreaAplicacion, schemas.AreaAplicacionBase)
generic_crud("terminos-clave", models.TerminoClave, schemas.TerminoClaveBase)
generic_crud("lineas-investigacion", models.LineaInvestigacion, schemas.LineaInvestigacionBase)
generic_crud("aliados", models.Aliado, schemas.AliadoBase)
generic_crud("tipos-producto", models.TipoProducto, schemas.TipoProductoBase)

# 8-10. Entidades Principales
generic_crud("docentes", models.Docente, schemas.DocenteBase)
generic_crud("proyectos", models.Proyecto, schemas.ProyectoBase)
generic_crud("productos", models.Producto, schemas.ProductoBase)

# 11-18. Tablas de Relación (Intermedias)
@app.post("/relaciones/asignar-docente-proyecto", tags=["Relaciones"])
def vincular_docente_proyecto(data: schemas.DesarrollaBase, db: Session = Depends(get_db)):
    nueva = models.Desarrolla(**data.model_dump())
    db.add(nueva); db.commit(); return {"msg": "Vinculación exitosa"}

# 19-21. Gestión de Usuarios
@app.get("/seguridad/usuarios", tags=["Seguridad"])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()

@app.post("/seguridad/usuarios", tags=["Seguridad"])
def crear_usuario(data: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    nuevo = models.Usuario(**data.model_dump())
    db.add(nuevo); db.commit(); db.refresh(nuevo)
    return nuevo

# --- COMPATIBILIDAD DASHBOARD ---
@app.get("/api/listar", tags=["Frontend"])
def api_listar_docentes(db: Session = Depends(get_db)):
    docentes = db.query(models.Docente).all()
    return [{"codigo": d.cedula, "nombre": f"{d.nombres} {d.apellidos}", "rol": d.cargo, "estado": "Activo"} for d in docentes]

from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")