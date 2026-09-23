from fastapi import FastAPI
from app.routers import items

app = FastAPI(title="Finder")

app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Finder is running!"}