from fastapi import FastAPI

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate

from operations.router import router as router_operation
from chat.router import router as chat_router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="TutorApp"
)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_operation)
app.include_router(chat_router)