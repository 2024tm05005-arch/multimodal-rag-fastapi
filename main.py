from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="Automotive Multimodal RAG API",
    description="Retrieval Augmented Generation system for automotive manuals",
    version="1.0"
)

app.include_router(router)