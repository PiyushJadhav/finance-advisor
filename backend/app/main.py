from fastapi import FastAPI
from app.routes import analyze, health

app = FastAPI(title="Finance Decision Advisor")

app.include_router(health.router)
app.include_router(analyze.router)