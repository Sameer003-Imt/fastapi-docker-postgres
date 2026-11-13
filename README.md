#FASTAPI + PostgreSQL with Docker Compose

A small practice project: a FastAPI web API and a PostgreSQL database, each running in its own Docker container.

## Run it
    docker compose up --build

Then open http://localhost:8000/visit. Every visit is saved in the database.

## What i learned
- Writing a Dockerfile for a python app
- Running several containers together with Docker Compose
- Connecting an API to a database by service name
- Keeping data between restarts with volumes

