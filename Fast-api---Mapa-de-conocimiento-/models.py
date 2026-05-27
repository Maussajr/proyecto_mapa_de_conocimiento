from sqlalchemy import Column, Integer, String, Date, ForeignKey, Double, Text, Boolean
from sqlalchemy.orm import relationship
from database import Base

class LineaInvestigacion(Base):
    __tablename__ = "linea_investigacion"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45), nullable=False)
    descripcion = Column(String(256), nullable=False)
    # Relación inversa
    docentes = relationship("Docente", back_populates="linea_rel")

class Docente(Base):
    __tablename__ = "docente"
    cedula = Column(Integer, primary_key=True)
    nombres = Column(String(60), nullable=False)
    apellidos = Column(String(60), nullable=False)
    genero = Column(String(12), nullable=False)
    cargo = Column(String(30), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    correo = Column(String(70), nullable=False)
    telefono = Column(String(20), nullable=False)
    url_cvlac = Column(String(128), nullable=False)
    fecha_actualizacion = Column(Date, nullable=False)
    escalafon = Column(String(45), nullable=False)
    perfil = Column(Text, nullable=False)
    cat_minciencia = Column(String(45))
    conv_minciencia = Column(String(45), nullable=False)
    nacionalidad = Column(String(45), nullable=False) # Corregido typo
    linea_investigacion_principal = Column(Integer, ForeignKey("linea_investigacion.id"))
    
    linea_rel = relationship("LineaInvestigacion", back_populates="docentes")

class Proyecto(Base):
    __tablename__ = "proyecto"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(70), nullable=False)
    resumen = Column(String(256), nullable=False)
    presupuesto = Column(Double, nullable=False)
    tipo_financiacion = Column(String(45), nullable=False)
    tipo_fondos = Column(String(45), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date)
    
    productos = relationship("Producto", backref="proyecto_rel")

class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    categoria = Column(String(45), nullable=False)
    fecha_entrega = Column(Date, nullable=False)
    proyecto_id = Column(Integer, ForeignKey("proyecto.id")) # Nombre explícito
    tipo_producto_id = Column(Integer, ForeignKey("tipo_producto.id"))