# 🌌 Star Wars GraphQL API – Challenge Back-End LQN 2025

API GraphQL construida con Django para crear y consultar información del universo Star Wars. Desarrollada como parte del Challenge Back-End – LQN.

---

## 🚀 Características principales

- ✅ API GraphQL con [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/) y soporte para [Relay](https://relay.dev/)
- ✅ Modelos: **Planet**, **Character**, **Movie**
- ✅ Queries y filtros
- ✅ Mutaciones para crear personajes, planetas y películas
- ✅ Despliegue local con Docker y Docker Compose

---

## 📦 Stack Tecnológico

- Python 3.11+
- Django
- GraphQL + Graphene-Django + Relay
- PostgreSQL
- Docker + Docker Compose

---

## 📂 Estructura del proyecto

```
├── docker-compose.yml
├── .env                      # Variables de entorno (ver abajo)
├── manage.py
├── README.md
├── requirements.txt
│
├── core/                     # Configuración general del proyecto
│   ├── __init__.py
│   ├── asgi.py
│   ├── schema.py             # Schema raíz de GraphQL
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── docker/                   # Infraestructura Docker
│   └── Dockerfile
│
├── helpers/                  # Filtros personalizados
│   └── filters.py
│
├── universe/                 # App principal
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── filters.py
│   ├── tests.py
│   ├── migrations/
│   │   └── 0001_initial.py
│   │
│   ├── models/               # Modelos divididos por entidad
│   │   ├── __init__.py
│   │   ├── character.py
│   │   ├── movie.py
│   │   └── planet.py
│   │
│   └── schemas/              # Schemas GraphQL
│       ├── __init__.py
│       ├── character.py
│       ├── movie.py
│       └── planet.py

```

---

## 🔌 Endpoint GraphQL

| Endpoint        | Descripción               |
|-----------------|---------------------------|
| `/graphql/`     | Punto de entrada GraphQL  |

Compatible con interfaces Relay.

---

## 🧬 Modelos

- **Planet**
  - `name`
- **Character**
  - `name`, `height`
- **Movie**
  - `title`, `opening_crawl`, `director`, `producers`, `created_date`, `planets`, `characters`

---

## ⚙️ Variables de entorno

Crea un archivo `.env` en la raíz con el siguiente contenido:

```env
POSTGRES_LOCAL_PORT=xxxx
POSTGRES_PORT=xxxx
POSTGRES_USER=xxxx
POSTGRES_PASSWORD=xxxx
POSTGRES_DB=xxxx
POSTGRES_HOST=xxxx

API_PORT=3000
API_CONTAINER_PORT=3000
```

---

## 🐳 Uso con Docker

### 1. Construcción y ejecución

```bash
docker compose -f .\docker-compose.yml --env-file .\.env up
```

### 2. Acceder a la API

Una vez iniciado, visita:  
📍 [http://localhost:3000/graphql/](http://localhost:3000/graphql/)

---

## 📌 Funcionalidades

### Queries + Filtros
- `allCharacters`: Lista personajes por nombre.
- `allMovies`: Lista todas las películas con datos completos.
- `allPlanets`: Lista todos los planetas.

### Mutaciones
- `createCharacter`
- `createMovie`
- `createPlanet`

---

## 📚 Recursos

- [GraphQL](https://graphql.org/)
- [Graphene](https://graphene-python.org/)

---

## 📄 Documentación

- Se generó la respectiva documentación del proyecto contenida dentro del endpoint inicial del proyecto

---

## 📤 Entrega

Este proyecto fue desarrollado como parte del **Challenge Back-End – LQN 2025**.  

---

## 🧠 Autor

Desarrollado por: [Javier Villarreal](https://www.linkedin.com/in/javier-villarreal1/)
