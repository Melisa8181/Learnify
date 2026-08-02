# Learnify 🚀 - Plataforma de Educación Online

Learnify es una plataforma web educativa diseñada para facilitar el registro de alumnos, la gestión de perfiles y la visualización de cursos interactivos. Combina un potente y vistoso diseño de interfaz de usuario con un backend ligero en Python/Flask y almacenamiento en la nube en tiempo real mediante Firebase.

---

## 🛠️ Tecnologías Utilizadas

### **Backend & Servidor**
*   **Python 3.x**: Lenguaje de programación principal.
*   **Flask**: Micro-framework para el enrutamiento y renderizado del lado del servidor.
*   **Jinja2**: Motor de plantillas dinámicas para la composición de vistas HTML.

### **Base de Datos & Almacenamiento**
*   **Firebase Realtime Database (NoSQL)**: Almacenamiento en la nube en formato JSON para el registro de usuarios y consulta del catálogo de cursos.

### **Frontend & UI/UX**
*   **HTML5 / CSS3 / JavaScript (ES6)**: Lenguajes core del frontend.
*   **Bootstrap 5**: Framework de estilos responsivo y moderno.
*   **jQuery**: Biblioteca de JavaScript para la manipulación del DOM y peticiones asíncronas (AJAX).
*   **Plugins & Animaciones**: 
    *   *Owl Carousel & Slick*: Deslizadores de imágenes interactivos.
    *   *Slicknav & Nice Select*: Interfaces pulidas de navegación y menús de selección.
    *   *FontAwesome & Flaticons*: Iconografía profesional.

---

## 📂 Estructura de Directorios

```text
Learnify/
├── templates/             # Plantillas HTML en Jinja2
│   ├── layout.html        # Plantilla principal del sitio (Header y Footer comunes)
│   ├── layout_alumnos.html# Plantilla para el panel interno de estudiantes
│   ├── home.html          # Vista de inicio con secciones interactivas
│   ├── about.html         # Sección de "Sobre Nosotros"
│   ├── contact.html       # Formulario de contacto integrado
│   ├── courses.html       # Catálogo estático/dinámico de cursos
│   ├── validar.html       # Pantalla de verificación de identidad (DNI) y registro
│   ├── login.html         # Pantalla de inicio de sesión de alumnos
│   ├── alumnos.html       # Panel de control de alumnos autenticados
│   ├── profile.html       # Vista y actualización de datos de perfil
│   └── cambiarcontrasenia.html # Plantilla para gestión alternativa de clave
├── static/                # Archivos estáticos (Assets)
│   ├── css/               # Estilos personalizados y de librerías (Bootstrap, Animate, etc.)
│   ├── js/                # Scripts de librerías y lógicas de interacción personalizada
│   ├── fonts/             # Tipografías y librerías de iconos
│   └── img/               # Recursos de imagen, banners y placeholders
├── index.py               # Archivo ejecutable principal del backend en Flask
└── .gitignore             # Exclusiones de Git (Ignora __pycache__ y temporales)
```

---

## 🌟 Características Clave

1.  **Enrutamiento Dinámico**: Uso eficiente de Flask para mapear URLs amigables hacia vistas renderizadas mediante Jinja2.
2.  **Verificación de Identidad**: Proceso en dos pasos que comprueba la existencia del DNI antes de habilitar el formulario de registro para evitar duplicados.
3.  **Visualización Personalizada**: El panel de alumnos (`alumnos.html`) consume servicios REST en Firebase de forma dinámica para mostrar la información del curso en el cual el estudiante se encuentra inscrito.
4.  **Gestión de Perfil Seguro**: En `profile.html` se valida la nueva contraseña usando expresiones regulares (mínimo 8 caracteres, mayúscula, número y símbolo especial) antes de guardarla.
5.  **Botón Flotante de WhatsApp**: Integración directa con la API de WhatsApp para facilitar el asesoramiento inmediato de potenciales estudiantes.

---

## 🔧 Instalación y Configuración Local

Sigue estos pasos para poner en marcha el proyecto en tu máquina local:

### **Requisitos Previos**
Asegúrate de tener instalado Python 3.x en tu sistema.

### **Paso 1: Clonar el Repositorio**
```bash
git clone https://github.com/tu-usuario/Learnify.git
cd Learnify
```

### **Paso 2: Crear y Activar un Entorno Virtual**
Es una buena práctica para mantener las dependencias aisladas:

*   **En Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
*   **En macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### **Paso 3: Instalar Dependencias**
Instala Flask y las librerías necesarias:
```bash
pip install Flask
```

*(Opcional) Si existe un archivo `requirements.txt`:*
```bash
pip install -r requirements.txt
```

### **Paso 4: Ejecutar el Servidor de Desarrollo**
Corre la aplicación de la siguiente manera:
```bash
python index.py
```

La aplicación estará disponible y escuchando peticiones en: `http://127.0.0.1:5000/` con la recarga automática activada (`debug=True`).

---

## 🔒 Buenas Prácticas de Seguridad y Escalabilidad (Hoja de Ruta)

Este proyecto fue desarrollado inicialmente como un prototipo funcional/MVP. Para llevarlo a un nivel de producción profesional, se recomiendan las siguientes mejoras:

1.  **Migrar la Lógica de Autenticación al Backend**: Actualmente, la verificación de credenciales y filtrado de usuarios se realiza en el cliente (JavaScript), lo cual expone la base de datos completa. Debe realizarse en `index.py` utilizando librerías como `Flask-Login` o tokens JWT.
2.  **Cifrado de Contraseñas**: Las claves de usuario deben ser encriptadas antes de guardarse en cualquier base de datos, utilizando algoritmos como `bcrypt` o `Argon2`. Nunca deben guardarse ni transmitirse en texto plano.
3.  **Proteger las URLs de la Base de Datos**: Mover las peticiones de Firebase al backend en Python de manera que los endpoints de base de datos se manejen mediante variables de entorno protegidas (`.env`) y no queden expuestas en el código del navegador.
4.  **Uso de Sesiones Seguras**: Controlar el acceso a `/alumnos` a través de sesiones de servidor (`flask.session`) en lugar de depender únicamente del parámetro `?id=` en la barra de direcciones de la URL, evitando la vulnerabilidad de secuestro de identificador.
