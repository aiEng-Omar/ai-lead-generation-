from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Lead Generation Agent")

app.include_router(router)