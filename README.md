## Caracteristicas

- **CRUD Generico**: Operaciones Create, Read, Update, Delete sobre las tablas 
- **Base de datos**: PostgreSQL
- **Arquitectura**: Separacion en 3 capas ( Models - Schemas -Main )

## Requisitos

| Requisito | Version |
|-----------|---------|
| Python | 3.11 o superior |
| pip | Ultima version |
| Git | Ultima version |
| Visual Studio Code | Ultima version  |
| Base de datos | PostgreSQL |

---

**Proceso para instalacion**

### 1. Clonar el repositorio

```bash
https://github.com/leandro9092/Fast-api---Mapa-de-conocimiento-.git
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual 

```bash
.\venv\Scripts\activate
```

### 4. Descargar dependencias 

```bash
pip install -r requirements.txt
```

### 5. Ejecutar la Api

```bash
python -m uvicorn main:app --reload
```

### 6. Abri documentacion 

http://127.0.0.1:8000/docs

### 7. Ingrensar al front end de la api 

http://127.0.0.1:8000/static/index.html