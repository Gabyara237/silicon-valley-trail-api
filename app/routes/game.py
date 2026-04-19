from fastapi import APIRouter

from app.dependencies import CurrentUserDep, GameServiceDep
from app.schemas.game import GameActionRequest, GameActionResult, GameEventRequest, GameResponse, GuestActionRequest, GuestGameActionResult, GuestGameCreate, GuestGameEventRequest, GuestGameResponse

router = APIRouter(prefix="/games", tags=["Game"])

@router.post("", response_model=GameResponse)
async def user_game(service: GameServiceDep, current_user: CurrentUserDep):
    return await service.create_game_for_user(current_user)

@router.post("/guest/actions", response_model=GuestGameActionResult)
async def apply_actions_guest(request:GuestActionRequest, service: GameServiceDep):
    return await service.apply_action_to_guest(request.game, request.action)

@router.post("/guest", response_model=GuestGameResponse)
def guest_game(game_data: GuestGameCreate, service: GameServiceDep):
    return service.create_guest_game(game_data.guest_username)

@router.post("/guest/events", response_model=GuestGameResponse)
def apply_event_to_guest( request: GuestGameEventRequest, service: GameServiceDep):
    return service.apply_event_to_guest(request.game, request.event, request.player_choice)


@router.post("/{game_id}/actions", response_model=GameActionResult, )
async def apply_actions(game_id: int, request: GameActionRequest, service: GameServiceDep, current_user: CurrentUserDep):
    return await service.apply_action_by_id(game_id, request.action, current_user)

@router.post("/{game_id}/events", response_model=GameResponse)
async def apply_event_to_user(game_id: int, request: GameEventRequest, service: GameServiceDep, current_user: CurrentUserDep):
   return await service.apply_event_by_id(game_id,request.event,request.player_choice, current_user)