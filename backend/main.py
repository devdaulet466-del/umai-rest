from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from api.router import router as api_router

app = FastAPI(title="UMAI Restaurant Menu API")

# Setup CORS to allow the Vue frontend to make requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For development, allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to UMAI Menu API. Use /api/menu to fetch options."}
