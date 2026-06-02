# Pizarra de Inspiración Interactiva (Full-Stack Dashboard)

## 📝 Descripción del Proyecto
Este proyecto consiste en una aplicación web Full-Stack integrada por un panel de control y una pizarra interactiva de notas. El ecosistema se comunica de forma asíncrona mediante una API REST local desarrollada en Python, la cual no solo administra recursos internos mediante Programación Orientada a Objetos (POO), sino que también consume servicios de terceros para inyectar contenido dinámico y motivacional ideal para entornos de estudio.

## 🛠️ Tecnologías y Herramientas Utilizadas

- **Backend:** Python 3.14, Flask (Framework web), Flask-CORS (Manejo de intercambio de recursos de origen cruzado).
- **Frontend:** HTML5 semántico, CSS3 moderno (con arquitectura basada en CSS Grid, Flexbox y variables dinámicas con estética Dark-Neon), JavaScript Asíncrono (ES6+).
- **Control de Versiones y Despliegue Local:** Git, GitHub, VS Code.
- **APIs Externas:** REST API de `adviceslip.com`.

## 🏗️ Arquitectura del Sistema: Métodos y Atributos (POO)
La lógica del backend fue desacoplada en clases independientes bajo principios de responsabilidad única, evitando scripts planos y garantizando escalabilidad:

### 1. Clase `Note`
Modela las notas individuales que se fijan en el tablero.

- **Atributos:** `id` *(int)*: Identificador único autogenerado para cada nota.
- `title` *(str)*: Título de la tarjeta de tareas.
- `content` *(str)*: Cuerpo o descripción de la nota.

- **Métodos:** `to_dict()`: Serializa las propiedades del objeto a un diccionario de Python para su posterior conversión a JSON.

### 2. Clase `Board`
Gestiona la colección de notas en la memoria del servidor.

- **Atributos:** `name` *(str)*: Nombre descriptivo de la pizarra.
- `notes` *(List[Note])*: Lista encapsulada que almacena instancias de la clase `Note`.

- **Métodos:** `add_note(note: Note)`: Añade una nueva instancia de nota al listado.
- `remove_note_by_id(note_id: int) -> bool`: Busca y remueve una nota específica basándose en su ID; retorna un booleano confirmando el éxito de la operación.
- `to_dict()`: Convierte la estructura completa del tablero y sus notas anidadas a un formato mapeable.

### 3. Clase `DashboardManager`
Controla las métricas de tiempo y personalización del inicio de sesión.

- **Atributos:** `username` *(str)*: Nombre del desarrollador que interactúa con el sistema.

- **Métodos:** `get_current_time_data()`: Obtiene la hora del sistema formateada (`HH:M:S`), el día actual y evalúa mediante estructuras de control condicionales un saludo personalizado dinámico según la jornada (Mañana, Tarde o Noche).

### 4. Clase `AdviceService`
Encapsula el consumo de servicios web externos.

- **Atributos:** `api_url` *(str)*: Endpoint base de la API externa.

- **Métodos:** `fetch_random_advice()`: Realiza una petición HTTP asíncrona mediante la librería `requests` a `adviceslip.com`. Cuenta con manejo de excepciones (`try/except`) para devolver un mensaje de contingencia en caso de fallas de red.

## 🚀 Desarrollo Paso a Paso: Lo que se construyó

1. **Diseño de Modelos (POO Backend):** Se crearon las abstracciones en `services.py` definiendo el comportamiento de los componentes mediante clases, constructores (`__init__`), encapsulamiento de datos y métodos de serialización.
2. **Construcción de la API REST (Flask):** En `app.py` se estructuró el servidor web, configurando políticas CORS para habilitar peticiones desde el navegador local y exponiendo las siguientes rutas funcionales:
   - `GET /api/board`: Entrega el estado del tablero y sus notas.
   - `GET /api/time`: Provee los datos de tiempo y saludos procesados.
   - `GET /api/advice`: Retorna el consejo síncrono obtenido de internet.
   - `POST /api/notes`: Recibe cargas JSON para instanciar y añadir notas dinámicamente.
   - `DELETE /api/notes/<id>`: Endpoint dinámico para la remoción de notas en memoria.
3. **Maquetación e Interfaz de Usuario (Frontend):** Se estructuró un tablero interactivo con CSS Grid utilizando una paleta de diseño de alto contraste basado en negros profundos, morados neón y verdes esmeralda. El diseño se adaptó para ser completamente responsivo.
4. **Consumo Asíncrono de Endpoints (JavaScript):** Se programó en `app.js` un ciclo de peticiones asíncronas con `fetch()`, `async/await` y manipulación dinámica del DOM. Se configuró un temporizador `setInterval` a 1000ms para mantener el segundero del reloj sincronizado con el backend, y manejadores de eventos (`EventListener`) para capturar formularios (`POST`) y disparar eliminaciones (`DELETE`).
5. **Control de Versiones Limpio:** Se configuró un archivo `.gitignore` global en la raíz del espacio de trabajo para excluir directorios de compilación y cachés temporales de Python (`__pycache__/`), inicializando el repositorio Git desde la raíz común del proyecto y subiendo de forma íntegra tanto la arquitectura del cliente como la del servidor a GitHub.
