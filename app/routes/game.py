from fastapi import APIRouter

from app.dependencies import CurrentUserDep, GameServiceDep
from app.schemas.game import GameResponse, GuestGameCreate, GuestGameResponse

router = APIRouter(prefix="/games", tags=["Game"])

@router.post("", response_model=GameResponse)
async def user_game(service: GameServiceDep, current_user: CurrentUserDep):
    return await service.create_game_for_user(current_user)

@router.post("/guest", response_model=GuestGameResponse)
async def guest_game(game_data: GuestGameCreate, service: GameServiceDep):
    return service.create_guest_game(game_data.guest_username)
