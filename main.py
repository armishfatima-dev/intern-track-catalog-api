from fastapi import FastAPI
from app.routers import catalog

app = FastAPI(
    title="InternTrack API Foundation",
    description="Program & Task Catalog REST API",
    version="1.0.0"
)

app.include_router(catalog.router)

@app.get("/")
def root():
    return {"message": "Welcome to InternTrack Program & Task Catalog API"}

