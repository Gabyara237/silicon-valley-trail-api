from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError


from app.core.game_actions import GAME_ACTION_EFFECTS, GameAction
from app.core.game_settings import DEFAULT_GAME_STATE
from app.core.game_utils import get_game_status, get_location_from_progress
from app.models.game import Game, GameStatus
from app.models.user import User


class GameService:
    def __init__(self, session: AsyncSession):
        self.session = session

    def _apply_action_effects_to_user(self, game:Game, action: GameAction):

        effects = GAME_ACTION_EFFECTS[action]

        game.team_energy += effects["team_energy"]
        game.cash += effects["cash"]
        game.bug_count += effects["bug_count"]
        game.caffeine += effects["caffeine"]
        game.market_traction += effects["market_traction"]
        game.travel_progress += effects["travel_progress"]
        game.current_day += effects["current_day"]

        game.team_energy = max(0, game.team_energy)
        game.cash = max(0, game.cash)
        game.bug_count = max(0, game.bug_count)
        game.caffeine = max(0, game.caffeine)
        game.market_traction = max(0, game.market_traction)
        game.travel_progress = min(100, max(0, game.travel_progress))

        game.current_location = get_location_from_progress(game.travel_progress)

        return game
    


    def _apply_action_effects_to_guest(self, game: dict, action: GameAction):

        effects = GAME_ACTION_EFFECTS[action]
        
        game["team_energy"] += effects["team_energy"]
        game["cash"] += effects["cash"]
        game["bug_count"] += effects["bug_count"]
        game["caffeine"] += effects["caffeine"]
        game["market_traction"] += effects["market_traction"]
        game["travel_progress"] += effects[action]["travel_progress"]
        game["current_day"] += effects["current_day"]
        

        game["team_energy"] = max(0, game["team_energy"])
        game["cash"] = max(0, game["cash"])
        game["bug_count"] = max(0, game["bug_count"])
        game["caffeine"] = max(0, game["caffeine"])
        game["market_traction"] = max(0, game["market_traction"])
        game["travel_progress"] = min(100, max(0, game["travel_progress"]))
    

        game["current_location"] = get_location_from_progress(game["travel_progress"])

        return game



    async def create_game_for_user(self, current_user: User)-> Game:

        game = Game(
            user_id = current_user.id, 

            status= DEFAULT_GAME_STATE["status"],
            current_location= DEFAULT_GAME_STATE["current_location"],
            
            cash= DEFAULT_GAME_STATE["cash"],
            current_day= DEFAULT_GAME_STATE["current_day"],
            team_energy = DEFAULT_GAME_STATE["team_energy"],
            bug_count= DEFAULT_GAME_STATE["bug_count"],
            caffeine= DEFAULT_GAME_STATE["caffeine"],
            market_traction= DEFAULT_GAME_STATE["market_traction"],
            travel_progress= DEFAULT_GAME_STATE["travel_progress"]
        )

        self.session.add(game)

        try:
            await self.session.commit()
            await self.session.refresh(game)
            return game
        
        except SQLAlchemyError:
            await self.session.rollback()

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Could not create game"
            )

    def create_guest_game(self, guest_username:str)-> dict:
        guest_username = guest_username.strip()

        if not guest_username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Guest username is required for guest players"
            )

        game = {
            "guest_username": guest_username,
            "status": DEFAULT_GAME_STATE["status"],
            "current_location": DEFAULT_GAME_STATE["current_location"],
            
            "cash": DEFAULT_GAME_STATE["cash"],
            "current_day": DEFAULT_GAME_STATE["current_day"],
            "team_energy": DEFAULT_GAME_STATE["team_energy"],
            "bug_count": DEFAULT_GAME_STATE["bug_count"],
            "caffeine": DEFAULT_GAME_STATE["caffeine"],
            "market_traction": DEFAULT_GAME_STATE["market_traction"],
            "travel_progress": DEFAULT_GAME_STATE["travel_progress"]
        }

        return game
    


    async def apply_action_by_id(self, game_id: int, action: GameAction) -> Game:
        game = await self.session.get(Game, game_id)

        if not game:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Game not found"
            )

        return await self.apply_action(game, action)
    

    async def apply_action(self, game: Game, action: GameAction )-> Game:

        if game.status != GameStatus.in_progress:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Game is already finished"
            )
        
        self._apply_action_effects_to_user(game,action)

        game.status= get_game_status(
            game.travel_progress,
            game.team_energy
        )
        
        try:
            await self.session.commit()
            await self.session.refresh(game)
            return game
        except SQLAlchemyError:
            await self.session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Could not apply action"
            )
    

    def apply_action_to_guest(self, game: dict, action: GameAction ) -> dict:

        if game["status"] != GameStatus.in_progress:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Game is already finished"
            )
        
        self._apply_action_effects_to_guest(game,action)
        
        game["status"]= get_game_status(
            game["travel_progress"],
            game["team_energy"]
        )
        
        return game

    

    


        
    