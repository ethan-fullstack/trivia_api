### 🚀 **¿Qué es FastAPI?**

**FastAPI** es un **microframework** de Python diseñado para crear **APIs modernas, rápidas y seguras**.  
Se basa en estándares abiertos:

- **OpenAPI** (para documentación automática).
    
- **JSON Schema** (para validación de datos).
    
- **Pydantic** (para manejar modelos y tipos).
    

Su principal ventaja es que usa **tipado moderno de Python (type hints)** para generar automáticamente la documentación y validar los datos de entrada y salida.

* * *

### ⚙️ **Arquitectura general de FastAPI**

Imagina FastAPI como un conjunto de componentes que se comunican entre sí:

```txt
Cliente (FrontEnd / Postman / Navegador)
        │
        ▼
  Uvicorn (Servidor ASGI)
        │
        ▼
  FastAPI (Framework principal)
        │
        ▼
  Lógica del negocio / Base de datos


```

#### 📍 Desglose:

1.  **Cliente:**  
    Envía una petición HTTP (GET, POST, PUT, DELETE) a una URL específica.  
    Ejemplo:
    
    `GET http://127.0.0.1:8000/users`
    
2.  **Uvicorn (Servidor ASGI):**  
    Es el **servidor** que recibe las peticiones y las pasa al framework FastAPI.  
    ASGI significa **Asynchronous Server Gateway Interface**, sucesor moderno de WSGI (usado por Django y Flask).  
    → Permite manejar muchas conexiones concurrentes (ideal para APIs rápidas).
    
3.  **FastAPI:**  
    Procesa la petición, ejecuta la función correspondiente (endpoint), y devuelve una **respuesta JSON**.
    
4.  **Base de datos o lógica de negocio:**  
    Aquí se ejecutan las operaciones reales (consultas, cálculos, validaciones).
    
5.  **Respuesta:**  
    FastAPI devuelve una **respuesta JSON estructurada**, que el cliente interpreta o muestra.
    

* * *

### 📡 **Flujo completo de una petición (visual)**

```txt
     ┌───────────────────────────────────────────────┐
     │                 CLIENTE                      │
     │ (Navegador, Postman, Frontend React, etc.)   │
     └──────────────┬────────────────────────────────┘
                    │  1️⃣ Petición HTTP
                    ▼
         ┌──────────────────────┐
         │      UVICORN         │
         │ (Servidor ASGI)      │
         └────────┬─────────────┘
                  │  2️⃣ Transfiere a FastAPI
                  ▼
         ┌──────────────────────┐
         │       FastAPI        │
         │ (Define rutas y      │
         │  ejecuta funciones)  │
         └────────┬─────────────┘
                  │  3️⃣ Ejecuta lógica del endpoint
                  ▼
         ┌──────────────────────┐
         │     Función Python   │
         │ (acceso a datos o    │
         │  respuesta estática) │
         └────────┬─────────────┘
                  │  4️⃣ Devuelve JSON
                  ▼
     ┌───────────────────────────────────────────────┐
     │              CLIENTE (recibe JSON)           │
     └───────────────────────────────────────────────┘

```

* * *

### 🧠 **Ejemplo básico del flujo**

Archivo `main.py`:

```python
# Importar FastAPI
from fastapi import FastAPI

# Crear una instancia de la aplicación
app = FastAPI()

# Definir una ruta con método GET
@app.get("/")
def read_root():
    # Respuesta JSON
    return {"message": "Welcome to my first FastAPI app!"}

```

* * *

### ▶️ **Ejecución con Uvicorn**

1.  **Abrir la terminal** dentro de la carpeta del proyecto.
    
2.  Ejecutar el comando:
    

`uvicorn main:app --reload`

Explicación del comando:

- `main` → nombre del archivo (sin `.py`).
    
- `app` → nombre de la instancia FastAPI creada (`app = FastAPI()`).
    
- `--reload` → recarga automática al guardar cambios (solo en desarrollo).
    

* * *

### 🌐 **Prueba en el navegador**

Abre en tu navegador:

- `http://127.0.0.1:8000/` → muestra el mensaje JSON.
    
- `http://127.0.0.1:8000/docs` → abre la documentación **Swagger UI**.
    
- `http://127.0.0.1:8000/redoc` → abre la documentación **ReDoc**.
    

* * *

### 💬 **Preguntas para reflexión**

- ¿Qué papel cumple Uvicorn dentro del ecosistema FastAPI?
    
- ¿Qué ventajas tiene ASGI frente a WSGI?
    
- ¿Por qué crees que FastAPI devuelve JSON por defecto?