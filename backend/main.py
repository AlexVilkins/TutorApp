from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from fastapi_users import fastapi_users
from fastapi.middleware.cors import CORSMiddleware

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.shemas import UserCreate, UserRead

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


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
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
