from fastapi import APIRouter

from app.dependencies import UserServiceDep
from app.schemas.user import UserCreate, UserResponse


router = APIRouter(prefix="/auth")

@router.post("/sign-up", response_model= UserResponse, status_code=201)
async def register_user(user: UserCreate, service: UserServiceDep):
    return await service.create_user(user)