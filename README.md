# 📚 Learnify - Plataforma de Educación Online

Una plataforma web educativa diseñada para facilitar el registro de alumnos, la gestión de perfiles de usuario y la visualización interactiva de cursos en línea.

🔗 **[Ver Deploy en Vivo (Render)](https://learnify-f23q.onrender.com/)**

---

## 📝 Descripción

**Learnify** es una aplicación web full-stack desarrollada originalmente como proyecto final integrador para el **Trayecto 3 de Potrero Digital**. El objetivo principal fue construir una plataforma educativa accesible, responsiva e interactiva que combinara un backend ágil con un frontend moderno y dinámico.

El sitio está estructurado en módulos y flujos clave:

- **Catálogo y Landing Educativa:** Presentación institucional, catálogo de cursos con descuentos, filtros interactivos y canal directo de asesoramiento vía WhatsApp.
- **Flujo de Verificación y Registro:** Validación previa por número de documento (DNI) para garantizar unicidad antes de habilitar el formulario de alta de usuario.
- **Panel de Alumnos (`alumnos.html`):** Área privada que consulta datos en tiempo real para mostrar el estado y los cursos específicos del estudiante.
- **Gestión de Perfil Seguro:** Vista de actualización de datos con validaciones estrictas en tiempo de ejecución (expresiones regulares para contraseñas seguras).

💡 _Nota de desarrollo:_ La aplicación fue adaptada y optimizada para producción, migrando dependencias a WSGI (`gunicorn`), estandarizando el enrutamiento estático y desplegando en Render con integración continua desde GitHub.

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.12 & Flask:** Micro-framework para el manejo de rutas backend, lógica de negocio y renderizado del lado del servidor mediante el motor de plantillas **Jinja2**.
- **HTML5 & CSS3:** Maquetación semántica, variables de estilo y diseño adaptable a múltiples resoluciones.
- **JavaScript (Vanilla JS & AJAX/Fetch):** Peticiones asíncronas para el consumo dinámico de datos y validaciones de formularios en el cliente.
- **Bootstrap 5 & Plugins UI:** Maquetación responsiva acompañada de librerías como _jQuery_, _Owl Carousel_, _Slick_, _Slicknav_, _Nice Select_ y _FontAwesome_.
- **Firebase Realtime Database (NoSQL):** Persistencia y consumo de información en la nube en formato JSON para el registro y consulta de cursos/alumnos.
- **Gunicorn:** Servidor HTTP WSGI para entornos de producción.

---

## 📂 Estructura del Proyecto

```text
Learnify/
├── templates/              # Vistas HTML renderizadas con Jinja2
│   ├── layout.html         # Plantilla base institucional (Navbar y Footer)
│   ├── layout_alumnos.html # Layout del dashboard de estudiantes
│   ├── home.html           # Página principal interactiva
│   ├── about.html          # Sección informativa institucional
│   ├── contact.html        # Formulario de contacto y consultas
│   ├── courses.html        # Catálogo dinámico de cursos
│   ├── validar.html        # Verificación previa de identidad (DNI)
│   ├── login.html          # Inicio de sesión de alumnos
│   ├── alumnos.html        # Panel de control del estudiante
│   ├── profile.html        # Perfil y actualización de credenciales
│   └── cambiarcontrasenia.html # Recuperación y cambio de clave
├── static/                 # Archivos y recursos estáticos
│   ├── css/                # Hojas de estilo personalizadas y de librerías
│   ├── js/                 # Scripts interactivos y plugins
│   ├── fonts/              # Tipografías e iconografía
│   └── img/                # Banners, placeholders y recursos gráficos
├── index.py                # Punto de entrada y servidor principal de Flask
├── requirements.txt        # Dependencias del entorno de producción
└── .gitignore              # Archivos y carpetas excluidos del control de versiones
```

---

## ⚙️ Instalación y Ejecución Local

Si querés clonar y ejecutar este proyecto en tu entorno local:

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/Melisa8181/Learnify.git
   cd Learnify
   ```

2. **Crear y activar un entorno virtual (recomendado):**
   - **En Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **En Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el servidor local:**
   ```bash
   python index.py
   ```
5. Abrí tu navegador en `http://127.0.0.1:5000/`.

---

## 🚧 Estado del Proyecto e Iteraciones Futuras

El proyecto se encuentra en producción y completamente operativo, con mejoras planificadas en seguridad y UX:

- [x] Migración y despliegue exitoso en Render con servidor WSGI (`gunicorn`).
- [x] Normalización de rutas absolutas para recursos estáticos (`/static/`).
- [ ] **Próximo paso:** Rediseñar visualmente las vistas de _Login_ y _Registro_ para alinearlas al resto del sistema.
- [ ] **Seguridad backend:** Migrar la autenticación de Firebase a sesiones seguras del lado del servidor (`flask.session` + `Flask-Login` y hashing de contraseñas).
- [ ] **Variables de entorno:** Mover endpoints y credenciales de configuración a un archivo `.env` protegido.
