# Learnify 🚀 - Plataforma de Educación Online

Learnify es una plataforma web educativa diseñada para facilitar el registro de alumnos, la gestión de perfiles y la visualización de cursos interactivos. Combina un potente y vistoso diseño de interfaz de usuario con un backend ligero en Python/Flask y almacenamiento en la nube en tiempo real mediante Firebase.

---

## 🛠️ Tecnologías Utilizadas

### **Backend & Servidor**

- **Python 3.x**: Lenguaje de programación principal.
- **Flask**: Micro-framework para el enrutamiento y renderizado del lado del servidor.
- **Jinja2**: Motor de plantillas dinámicas para la composición de vistas HTML.

### **Base de Datos & Almacenamiento**

- **Firebase Realtime Database (NoSQL)**: Almacenamiento en la nube en formato JSON para el registro de usuarios y consulta del catálogo de cursos.

### **Frontend & UI/UX**

- **HTML5 / CSS3 / JavaScript (ES6)**: Lenguajes core del frontend.
- **Bootstrap 5**: Framework de estilos responsivo y moderno.
- **jQuery**: Biblioteca de JavaScript para la manipulación del DOM y peticiones asíncronas (AJAX).
- **Plugins & Animaciones**:
  - _Owl Carousel & Slick_: Deslizadores de imágenes interactivos.
  - _Slicknav & Nice Select_: Interfaces pulidas de navegación y menús de selección.
  - _FontAwesome & Flaticons_: Iconografía profesional.

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

- **En Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
- **En macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### **Paso 3: Instalar Dependencias**

Instala Flask y las librerías necesarias:

```bash
pip install Flask
```

_(Opcional) Si existe un archivo `requirements.txt`:_

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

## 🚧 Roadmap Técnico (Mejoras a Producción)

Este proyecto fue desarrollado como un MVP funcional. A continuación se detallan mejoras planificadas para llevarlo a un entorno productivo, enfocadas en seguridad, escalabilidad y buenas prácticas de arquitectura:

### 🔐 Seguridad

- Migrar la autenticación al backend utilizando Flask (por ejemplo con Flask-Login o JWT), evitando exponer la base de datos en el cliente.
- Implementar hashing seguro de contraseñas (bcrypt / Argon2).
- Gestionar credenciales y endpoints sensibles mediante variables de entorno (`.env`).

### 🧱 Arquitectura

- Centralizar la lógica de acceso a datos en el backend, desacoplando frontend y base de datos.
- Definir endpoints específicos para consultas en lugar de exponer nodos completos de Firebase.

### 🔑 Manejo de sesiones

- Implementar sesiones seguras del lado del servidor (`flask.session`) para controlar autenticación y autorización.
- Evitar el uso de parámetros en URL (`?id=`) como mecanismo de identificación.

### 📈 Escalabilidad

- Optimizar consultas a base de datos para evitar cargas completas en memoria del cliente.
- Evaluar migración a una arquitectura más robusta (API REST dedicada).
