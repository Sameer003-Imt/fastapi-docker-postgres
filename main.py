import os
import psycopg
from fastapi import FastAPI

DB_URL = os.environ["DATABASE_URL"]
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI in Docker!"}

@app.get("/visit")
def visit():
    with psycopg.connect(DB_URL) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS visits (id SERIAL PRIMARY KEY, time TIMESTAMP DEFAULT NOW())")
        conn.execute("INSERT INTO visits DEFAULT VALUES")
        count = conn.execute("SELECT COUNT(*) FROM visits").fetchone()[0]
    return {"visits": count}
