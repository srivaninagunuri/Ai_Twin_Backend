from fastapi import FastAPI
from app.database import engine, Base
from app.models.twin_model import Twin
from app.routers.twin_router import router

app = FastAPI(
    title="AI Twin Backend",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "AI Twin Backend Running Successfully"
    }