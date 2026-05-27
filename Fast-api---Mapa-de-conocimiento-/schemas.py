from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, List


class AreaConocimientoBase(BaseModel):
    id: int
    gran_area: str
    area: str
    disciplina: str
    class Config: from_attributes = True

class ODSBase(BaseModel):
    id: int
    nombre: str
    categoria: str
    class Config: from_attributes = True

class AreaAplicacionBase(BaseModel):
    id: int
    nombre: str
    class Config: from_attributes = True

class TerminoClaveBase(BaseModel):
    termino: str
    termino_ingles: Optional[str] = None
    class Config: from_attributes = True

class LineaInvestigacionBase(BaseModel):
    id: Optional[int] = None
    nombre: str
    descripcion: str
    class Config: from_attributes = True

class AliadoBase(BaseModel):
    nit: int
    razon_social: str
    nombre_contacto: str
    correo: str
    telefono: str
    ciudad: str
    class Config: from_attributes = True

class TipoProductoBase(BaseModel):
    id: int
    categoria: str
    clase: str
    nombre: str
    tipologia: str
    class Config: from_attributes = True

# --- ENTIDADES PRINCIPALES ---
class DocenteBase(BaseModel):
    cedula: int
    nombres: str
    apellidos: str
    genero: str
    cargo: str
    fecha_nacimiento: date
    correo: str
    telefono: str
    url_cvlac: str
    fecha_actualizacion: date
    escalafon: str
    perfil: str
    conv_minciencia: str
    nacionalidaad: str
    cat_minciencia: Optional[str] = None
    linea_investigacion_principal: Optional[int] = None
    class Config: from_attributes = True

class ProyectoBase(BaseModel):
    id: int
    titulo: str
    resumen: str
    presupuesto: float
    tipo_financiacion: str
    tipo_fondos: str
    fecha_inicio: date
    fecha_fin: Optional[date] = None
    class Config: from_attributes = True

class ProductoBase(BaseModel):
    id: int
    nombre: str
    categoria: str
    fecha_entrega: date
    proyecto: Optional[int] = None
    tipo_producto: int
    class Config: from_attributes = True


class UsuarioCreate(BaseModel):
    username: str
    password: str
    email: str
    activo: bool = True

class RolBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None


class DesarrollaBase(BaseModel):
    docente: int
    proyecto: int
    rol: str
    descripcion: str