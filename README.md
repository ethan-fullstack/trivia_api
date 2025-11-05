# README · Semana 4 · Día 1

**Tema:** Introducción práctica a FastAPI (microframework) y comparación con Django (full framework).

**Objetivo del día:** Comprender qué es un framework, diferenciar microframework vs. full framework, entender la arquitectura básica de FastAPI (ASGI/Starlette/Pydantic) y ejecutar una API local con Uvicorn. Además, explorar la **documentación automática** (Swagger UI y ReDoc).

---

## 📚 Tabla de contenido

### Archivos de apoyo (carpeta `guide/`)

- [¿Qué es un Framework?](guides/framework_101.md)
- [¿Qué es FastAPI?](guides/arquitectura.md)

### Secciones de este README

- [1. ¿Qué es un _framework_?](#1-qué-es-un-framework)
- [2. Microframework vs _Full framework_: FastAPI vs Django](#2-microframework-vs-full-framework-fastapi-vs-django)
- [3. Arquitectura básica de FastAPI](#3-arquitectura-básica-de-fastapi)
- [4. Ejecución con Uvicorn (y alternativa `fastapi dev`)](#4-ejecución-con-uvicorn-y-alternativa-fastapi-dev)
- [5. Documentación automática: `/docs`, `/redoc` y `openapi.json`](#5-documentación-automática-docs-redoc-y-openapijson)
- [6. Ejemplos mínimos comprobables](#6-ejemplos-mínimos-comprobables)
- [7. Buenas prácticas y checklist de evidencias](#7-buenas-prácticas-y-checklist-de-evidencias)
- [8. Preguntas guía para la reflexión](#8-preguntas-guía-para-la-reflexión)
- [9. Referencias oficiales](#9-referencias-oficiales)

---

## 1) ¿Qué es un _framework_?

Un **framework** es un conjunto de componentes reutilizables (librerías, utilidades, convenciones y plantillas) que **aceleran** y **estandarizan** el desarrollo. En backend, un framework suele resolver:

- Enrutamiento (rutas/URLs ➜ funciones/controladores).
- Manejo de peticiones/respuestas HTTP.
- Validación y serialización de datos.
- Integración con herramientas de documentación, seguridad, sesiones, etc.

> **Idea clave:** un framework establece una **arquitectura base** y te deja concentrarte en **la lógica de negocio**.

---

## 2) Microframework vs _Full framework_: FastAPI vs Django

### Microframework (FastAPI)

- Núcleo **ligero** y **enfocado** en APIs HTTP modernas.
- Se apoya en estándares y proyectos especializados:
  - **ASGI** para la interfaz servidor-app asíncrona.
  - **Starlette** para la capa web (ruteo, middleware, etc.).
  - **Pydantic** para validación/serialización basada en _type hints_.
- **Escalable por composición:** tú eliges ORM, autenticación, plantillas, etc.
- **Documentación automática** de API basada en **OpenAPI**.

### _Full framework_ (Django)

- Baterías incluidas: ORM propio, migraciones, sistema de autenticación, administración, plantillas, formularios, internacionalización, etc.
- Ideal para proyectos con **múltiples capas** (HTML, admin, forms) o equipos que buscan **productividad con convenciones**.
- Para APIs REST, suele usarse **Django REST Framework** (DRF) sobre Django.

### ¿Cuándo escoger cada uno?

- **FastAPI**: microservicios, APIs de alto rendimiento, integraciones con _async_, validación estricta, documentación instantánea.
- **Django (+DRF)**: portales completos, backoffice con admin, dominio de datos complejo, equipo que aprovecha las herramientas integradas.

> **Conclusión:** FastAPI y Django no compiten tanto como se complementan. En este trimestre, **comenzamos con FastAPI** por su curva de aprendizaje clara para APIs y su documentación automática; más adelante **veremos DRF** para un backend integral.

---

## 3) Arquitectura básica de FastAPI

FastAPI se **construye sobre Starlette** (capa web ASGI) e integra **Pydantic** para validar y serializar datos a partir de **anotaciones de tipo** (_type hints_) de Python. El servidor de desarrollo/producción más común es **Uvicorn**, un servidor **ASGI**.

**Diagrama conceptual (simplificado):**

```
Cliente (navegador/Thunder/Postman)
        │  HTTP/1.1 - HTTP/2 - WebSocket
        ▼
Servidor ASGI (Uvicorn)
        │  Llama a la app según el protocolo (ASGI)
        ▼
Starlette (ruteo, middleware, respuestas)
        │  FastAPI extiende Starlette
        ▼
FastAPI (decoradores, dependencias, validación)
        │  Modelado y validación
        ▼
Pydantic (modelos y JSON Schema)
        │  (tu lógica/DB)
        ▼
Capa de negocio / persistencia
```

**Puntos clave:**

- **ASGI** (Asynchronous Server Gateway Interface) es la interfaz moderna que habilita **concurrencia** y protocolos como **HTTP/2** y **WebSocket**.
- **Uvicorn** es un servidor ASGI popular y liviano.
- **Starlette** provee ruteo, _middleware_, respuestas, _background tasks_, etc.
- **FastAPI** hereda de Starlette y añade decoradores, _dependency injection_, validación automática, generación de OpenAPI, etc.
- **Pydantic** genera esquemas JSON (JSON Schema) a partir de los modelos/tipos que defines; FastAPI los usa para tu **esquema OpenAPI**.

---

## 4) Ejecución con Uvicorn (y alternativa `fastapi dev`)

### Opción A) Comando recomendado en desarrollo

```bash
fastapi dev main.py
```

- Arranca un servidor de desarrollo **con recarga** automática.
- Detecta tu módulo y la instancia `app` sin que tengas que escribir `main:app`.

### Opción B) Uvicorn directamente

```bash
uvicorn main:app --reload
```

- `main` es el nombre del archivo (sin `.py`).
- `app` es la instancia creada con `app = FastAPI()`.
- `--reload` hace _hot-reload_ en desarrollo.

> Ambas opciones levantan la app típicamente en `http://127.0.0.1:8000/` y verás en la consola algo como: `Uvicorn running on http://127.0.0.1:8000`.

---

## 5) Documentación automática: `/docs`, `/redoc` y `openapi.json`

FastAPI genera un **esquema OpenAPI 3.1** de tu API y, a partir de él, expone **dos UIs** por defecto:

- **Swagger UI** en `http://127.0.0.1:8000/docs` (interactiva, ideal para probar _endpoints_).
- **ReDoc** en `http://127.0.0.1:8000/redoc` (navegación estructurada más técnica).

Además, puedes ver el **esquema bruto** en:

- `http://127.0.0.1:8000/openapi.json`

> **¿Por qué es valioso?**
>
> - Facilita pruebas manuales sin Postman/Thunder.
> - Sirve de contrato vivo para frontend/mobile.
> - Permite **generar SDKs/clients** automáticamente con herramientas del ecosistema OpenAPI.

---

## 6) Ejemplos mínimos comprobables

> **Regla del curso:** el código va en **inglés**, los comentarios y explicaciones en **español**.

### `main.py` — _Hello FastAPI_

```python
from fastapi import FastAPI

app = FastAPI(title="Hello FastAPI", version="1.0")

@app.get("/")
def read_root():
    """Respuesta JSON mínima para comprobar el servidor."""
    return {"message": "Hello, ADSO!"}
```

**Ejecutar (elige una):**

```bash
fastapi dev main.py
# o
uvicorn main:app --reload
```

Ahora abre:

- `http://127.0.0.1:8000/` → `{ "message": "Hello, ADSO!" }`
- `http://127.0.0.1:8000/docs` → Swagger UI
- `http://127.0.0.1:8000/redoc` → ReDoc

### Validación con Pydantic (request/response)

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Sample with Pydantic", version="1.0")

# Modelo de entrada: crea un ítem
class ItemCreate(BaseModel):
    name: str = Field(..., min_length=3)
    tags: List[str] = Field(default_factory=list)

# Modelo de salida: muestra un ítem con ID asignado
class Item(BaseModel):
    id: int
    name: str
    tags: List[str]

items_db: List[Item] = []

@app.post("/items", response_model=Item)
def create_item(payload: ItemCreate):
    """Valida la entrada con Pydantic y devuelve un objeto tipado."""
    new = Item(id=len(items_db) + 1, **payload.dict())
    items_db.append(new)
    return new
```

Este endpoint aparece **documentado automáticamente** (esquema de entrada/salida) en `/docs` y `/redoc`.

---

## 7) Buenas prácticas y checklist de evidencias

**Buenas prácticas (Día 1):**

- Usa entorno virtual (`python -m venv venv` y activar) y congela dependencias con `requirements.txt`.
- Nombra tu instancia `app` y mantén `main.py` simple.
- Añade `response_model` en endpoints para **esquemas claros**.
- Empieza con `fastapi dev` (o `uvicorn --reload`) y verifica los logs.
- Pon atención a **códigos HTTP** y mensajes ordenados.

**Checklist de evidencias:**

- [ ] Proyecto ejecuta en `http://127.0.0.1:8000/`.
- [ ] Swagger UI y ReDoc accesibles.
- [ ] Al menos un endpoint `GET` y uno `POST` con modelos Pydantic.
- [ ] Capturas de pantalla (o video corto) de la API en funcionamiento.

---

## 8) Preguntas guía para la reflexión

1. ¿Qué ventajas prácticas aporta un microframework como FastAPI frente a programar todo “a mano”?
2. ¿Qué entiendes por **ASGI** y por qué es relevante hoy (HTTP/2, WebSocket, _async_)?
3. ¿Qué representa el **esquema OpenAPI** y cómo se traduce en `/docs` y `/redoc`?
4. ¿Cómo te ayuda Pydantic a **prevenir errores** de datos desde el día 1?

---

## 9) Referencias oficiales

> Documentación oficial y estándares (consulta siempre estas fuentes):

- FastAPI – Tutorial/First Steps: https://fastapi.tiangolo.com/tutorial/first-steps/
- FastAPI – Tutorial (ES): https://fastapi.tiangolo.com/es/tutorial/
- Uvicorn – Sitio y documentación: https://uvicorn.dev/
- ASGI – Especificación: https://asgi.readthedocs.io/
- Starlette – Introducción: https://starlette.dev/
- Pydantic – Documentación (v2): https://docs.pydantic.dev/latest/
- Django – Documentación (5.2): https://docs.djangoproject.com/en/5.2/
- OpenAPI – Sitio de la iniciativa: https://www.openapis.org/
- OpenAPI Specification 3.1: https://swagger.io/specification/

---

> **Nota pedagógica (ADSO):** En este día trabajamos con datos en memoria para comprender la arquitectura y el _tooling_. Más adelante integraremos bases de datos, autenticación y despliegue, y compararemos este flujo con **Django REST Framework** para un backend integral.
