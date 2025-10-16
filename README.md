# 📚 Gestor de Editorial API (EditorialHub API)

`EditorialHub API` es un servicio RESTful construido con Django y Django REST Framework que permite gestionar una base de datos de libros y sus editoriales. La API ofrece endpoints para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en ambos recursos.

---

## ✨ Características

* CRUD completo para la gestión de **Libros**.
* CRUD completo para la gestión de **Editoriales**.
* Relación entre Libros y Editoriales.
* Endpoint de búsqueda para filtrar libros por **título** o **género**.
* Respuestas JSON personalizadas para una mejor experiencia de desarrollo.

---

## 💻 Tecnologías Usadas

* **Python**
* **Django**
* **Django REST Framework**

---

## 🚀 Instalación y Ejecución Local

Sigue estos pasos para levantar el proyecto en tu máquina local.

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/editorialhub_api.git](https://github.com/TU_USUARIO/editorialhub_api.git)
    cd editorialhub_api
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # Crear el entorno
    python -m venv venv

    # Activar en Windows
    .\venv\Scripts\activate

    # Activar en macOS/Linux
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Asegúrate de crear un archivo `requirements.txt` con `pip freeze > requirements.txt`)*

4.  **Aplica las migraciones a la base de datos:**
    ```bash
    python manage.py migrate
    ```

5.  **Inicia el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    La API estará disponible en `http://127.0.0.1:8000/api/`

---

## 📡 Endpoints de la API

La URL base para todos los endpoints es `/api/`.

### Editoriales (`/api/editoriales/`)

#### `GET /api/editoriales/`
Obtiene un listado de todas las editoriales.

* **Ejemplo con `curl`:**
    ```bash
    curl -X GET [http://127.0.0.1:8000/api/editoriales/](http://127.0.0.1:8000/api/editoriales/)
    ```

#### `POST /api/editoriales/`
Crea una nueva editorial.

* **Ejemplo con `curl`:**
    ```bash
    curl -X POST [http://127.0.0.1:8000/api/editoriales/](http://127.0.0.1:8000/api/editoriales/) \
    -H "Content-Type: application/json" \
    -d '{"nombre": "Anagrama", "pais": "España"}'
    ```

#### `GET /api/editoriales/{id}/`
Obtiene los detalles de una editorial específica.

* **Ejemplo con `curl`:**
    ```bash
    curl -X GET [http://127.0.0.1:8000/api/editoriales/1/](http://127.0.0.1:8000/api/editoriales/1/)
    ```

#### `PUT /api/editoriales/{id}/`
Actualiza completamente una editorial existente.

* **Ejemplo con `curl`:**
    ```bash
    curl -X PUT [http://127.0.0.1:8000/api/editoriales/1/](http://127.0.0.1:8000/api/editoriales/1/) \
    -H "Content-Type: application/json" \
    -d '{"nombre": "Editorial Anagrama", "pais": "España"}'
    ```

#### `DELETE /api/editoriales/{id}/`
Elimina una editorial.

* **Ejemplo con `curl`:**
    ```bash
    curl -X DELETE [http://127.0.0.1:8000/api/editoriales/1/](http://127.0.0.1:8000/api/editoriales/1/)
    ```
---
### Libros (`/api/libros/`)

#### `GET /api/libros/`
Obtiene un listado de todos los libros.

* **Ejemplo con `curl`:**
    ```bash
    curl -X GET [http://127.0.0.1:8000/api/libros/](http://127.0.0.1:8000/api/libros/)
    ```

#### `POST /api/libros/`
Crea un nuevo libro, asociándolo a una editorial existente por su `id`.

* **Ejemplo con `curl`:**
    ```bash
    curl -X POST [http://127.0.0.1:8000/api/libros/](http://127.0.0.1:8000/api/libros/) \
    -H "Content-Type: application/json" \
    -d '{"titulo": "El Desierto de los Tártaros", "genero": "Novela", "año": 1940, "editorial": 1}'
    ```

#### `GET /api/libros/?search={termino}`
Busca libros cuyo título o género contenga el término de búsqueda.

* **Ejemplo con `curl`:**
    ```bash
    # Buscar por título
    curl -X GET "[http://127.0.0.1:8000/api/libros/?search=Desierto](http://127.0.0.1:8000/api/libros/?search=Desierto)"
    
    # Buscar por género
    curl -X GET "[http://127.0.0.1:8000/api/libros/?search=Novela](http://127.0.0.1:8000/api/libros/?search=Novela)"
    ```

#### `GET /api/libros/{id}/`
Obtiene los detalles de un libro específico.

* **Ejemplo con `curl`:**
    ```bash
    curl -X GET [http://127.0.0.1:8000/api/libros/1/](http://127.0.0.1:8000/api/libros/1/)
    ```

#### `PUT /api/libros/{id}/`
Actualiza un libro existente.

* **Ejemplo con `curl`:**
    ```bash
    curl -X PUT [http://127.0.0.1:8000/api/libros/1/](http://127.0.0.1:8000/api/libros/1/) \
    -H "Content-Type: application/json" \
    -d '{"titulo": "El Desierto de los Tártaros", "genero": "Existencialismo", "año": 1940, "editorial": 1}'
    ```

#### `DELETE /api/libros/{id}/`
Elimina un libro.

* **Ejemplo con `curl`:**
    ```bash
    curl -X DELETE [http://127.0.0.1:8000/api/libros/1/](http://127.0.0.1:8000/api/libros/1/)
    ```