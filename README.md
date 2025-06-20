# 🛠️ Django Base Project

Proyecto base para aplicaciones web y APIs en Django + PostgreSQL + Docker + Django REST Framework. Ideal como punto de partida profesional para nuevos proyectos.

---

## 🚀 Características

- Django 4.x con configuración separada por entorno (`dev`, `prod`)
- Django REST Framework listo para usar
- PostgreSQL usando Docker
- Variables de entorno con `.env`
- Pruebas automáticas integradas con GitHub Actions
- `Makefile` con comandos útiles
- Estructura modular y mantenible

---

## 📦 Requisitos

- Python 3.11+
- Docker y Docker Compose
- `make` (GNU Make)

---

## ⚙️ Instalación y configuración

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/django-base-project.git
cd django-base-project
```


### 2. Configura el archivo `.env`

Crea un archivo `.env` con el siguiente contenido:

```
SECRET_KEY=tu_clave_secreta
DEBUG=True

DB_NAME=django_db
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5432
```

### 3. Levanta la base de datos con Docker

```bash
docker compose up -d
```

### 4. Inicializa entorno virtual e instala dependencias

```bash
make init
```

### 5. Ejecuta migraciones y crea usuario admin

```bash
make migrate
make superuser
```

### 6. Corre el servidor

```bash
make run
```

Abre tu navegador: http://localhost:8000 

## 🧪 Ejecutar pruebas
```bash
make test
```

Las pruebas también se ejecutan automáticamente en GitHub Actions al hacer push a `main`.

## 📁 Estructura del proyecto
```
django-base-project/
├── config/               # Configuración principal de Django
│   └── settings/         # Archivos separados por entorno
├── core/                 # Aplicación principal (ejemplo: Book API)
├── .env                  # Variables de entorno
├── docker-compose.yml    # PostgreSQL en Docker
├── Makefile              # Comandos útiles
└── requirements.txt      # Dependencias
```

## 🔐 Autenticación (pendiente)
```
Integración con JWT usando djangorestframework-simplejwt (opcional).
```

## 📦 Próximas mejoras
- Autenticación con JWT
- Gestión de permisos por grupos
- Dockerfile para entorno completo
- Deploy automático a Railway/Render/Heroku

## 🧑‍💻 Autor
Edgar Fernando Carrión Ccoicca
Repositorio: github.com/efccc0010