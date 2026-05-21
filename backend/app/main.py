from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.predict_routes import router as predict_router
from app.routes.clean_routes import router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(router)
app.include_router(
    predict_router
)