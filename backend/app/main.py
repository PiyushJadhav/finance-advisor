from fastapi import FastAPI
from app.routes import analyze, health
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Finance Decision Advisor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze.router, tags=["analyze"])
app.include_router(health.router, tags=["health"])

@app.get("/")
async def root():
    return {"message": "Finance Decision Advisor API", "status": "running"}