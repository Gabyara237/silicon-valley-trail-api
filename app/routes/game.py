from fastapi import APIRouter

from app.dependencies import CurrentUserDep, GameServiceDep
from app.schemas.game import GameActionRequest, GameActionResult, GameEventRequest, GameResponse, GuestActionRequest, GuestGameActionResult, GuestGameCreate, GuestGameEventRequest, GuestGameResponse
from app.services.ai_advice import AIAdviceService

router = APIRouter(prefix="/games", tags=["Game"])

@router.post("/new", response_model=GameResponse)
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


@router.get("/active")
async def get_active_game(service: GameServiceDep, current_user: CurrentUserDep):
    active_game = await service.get_active_game(current_user)

    if not active_game:
        return {"active_game": None}

    return {
        "active_game": {
            "id": active_game.id,
            "status": active_game.status
        }
    }


@router.post("/{game_id}/abandon", response_model=GameResponse)
async def abandon_game(game_id: int, service: GameServiceDep, current_user:CurrentUserDep):
    return await service.abandon_game(game_id,current_user)

@router.post("/{game_id}/save", response_model=GameResponse)
async def save_game(game_id: int,service: GameServiceDep, current_user: CurrentUserDep):
    return await service.save_game(game_id,current_user)

@router.post("/{game_id}/resume", response_model=GameResponse)
async def resume_game(game_id: int, service: GameServiceDep, current_user: CurrentUserDep):
    return await service.resume_game(game_id,current_user)

@router.post("/{game_id}/actions", response_model=GameActionResult)
async def apply_actions(game_id: int, request: GameActionRequest, service: GameServiceDep, current_user: CurrentUserDep):
    return await service.apply_action_by_id(game_id, request.action, current_user)

@router.post("/{game_id}/events", response_model=GameResponse)
async def apply_event_to_user(game_id: int, request: GameEventRequest, service: GameServiceDep, current_user: CurrentUserDep):
   return await service.apply_event_by_id(game_id,request.event,request.player_choice, current_user)



@router.post("/{game_id}/advice")
async def get_game_advice(game_id: int, service: GameServiceDep, current_user: CurrentUserDep,):
    
    game = await service.get_game_by_id_for_user(game_id, current_user)
    advice_service = AIAdviceService()
    advice = advice_service.get_advice(game)
    return {"advice": advice}