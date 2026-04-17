from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError


from app.core.game_settings import DEFAULT_GAME_STATE
from app.models.game import Game
from app.models.user import User


class GameService:
    def __init__(self, session: AsyncSession):
        self.session = session

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
        
    