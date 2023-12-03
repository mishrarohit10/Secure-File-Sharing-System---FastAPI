from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from fastapi.staticfiles import StaticFiles

auth_scheme = HTTPBearer()

from app.config import settings
from app.routers import auth, user, files

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=['Auth'], prefix='/auth')
app.include_router(user.router, tags=['Users'], prefix='/users')
app.include_router(files.router, tags=['Files'], prefix='/files')

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/healthcheck")
def root():
    return {"message": "OK"}
