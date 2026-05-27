from sqlalchemy import Column, Integer, String, Date, ForeignKey, Double, Text
from sqlalchemy.orm import relationship
from database import Base

class LineaInvestigacion(Base):
    __tablename__ = "linea_investigacion"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45), nullable=False)
    descripcion = Column(String(256), nullable=False)
    docentes = relationship("Docente", back_populates="linea_rel")

class Docente(Base):
    __tablename__ = "docente"
    cedula = Column(Integer, primary_key=True)
    nombres = Column(String(60), nullable=False)
    linea_investigacion_principal = Column(Integer, ForeignKey("linea_investigacion.id"))
    linea_rel = relationship("LineaInvestigacion", back_populates="docentes")

class Proyecto(Base):
    __tablename__ = "proyecto"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(70), nullable=False)
    productos = relationship("Producto", backref="proyecto_rel")

class TipoProducto(Base):
    __tablename__ = "tipo_producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    productos = relationship("Producto", backref="tipo_producto_rel")

class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    proyecto_id = Column(Integer, ForeignKey("proyecto.id"))
    tipo_producto_id = Column(Integer, ForeignKey("tipo_producto.id"))

class AreaConocimiento(Base):
    __tablename__ = "area_conocimiento"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

class ObjetivoDesarrolloSostenible(Base):
    __tablename__ = "ods"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)