from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.locations import router as locations_router

app = FastAPI(title="NewEdg API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200",
        "https://newedg-dab9a.web.app/",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Note:
# For Cloud Run / production, replace allow_origins with your deployed frontend URL (e.g. Firebase hosting domain).
# Keeping localhost here is only for local development.

@app.get("/")
def root():
    return {"message": "API is running"}

app.include_router(locations_router)