from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies import UserServiceDep, AuthServiceDep
from app.schemas.user import UserCreate, UserResponse


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/sign-up", response_model= UserResponse, status_code=201)
async def register_user(user: UserCreate, service: UserServiceDep):
    return await service.create_user(user)

@router.post("/sign-in")
async def login_user(request_form: Annotated[OAuth2PasswordRequestForm, Depends()], service: AuthServiceDep):

    token = await service.login(request_form.username,request_form.password)

    return{
        "access_token": token,
        "token_type": "bearer"
    }
