from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError


from app.core.environment import get_traffic_effect
from app.core.game_actions import GAME_ACTION_EFFECTS, GameAction
from app.core.game_events import GAME_EVENTS, get_hackathon_outcome, get_weather_effect, maybe_get_event
from app.core.game_settings import DEFAULT_GAME_STATE
from app.core.game_utils import get_coordinates_from_location, get_game_status, get_location_from_progress, get_milestone_by_location


from app.integrations.google_routes_client import get_traffic
from app.integrations.weather_client import get_weather
from app.models.game import Game, GameStatus
from app.models.game_event import EventChoice, EventType, GameEvent
from app.models.user import User
from app.schemas.game import DataTraffic, Weather


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
        game["travel_progress"] += effects["travel_progress"]
        game["current_day"] += effects["current_day"]
        

        game["team_energy"] = max(0, game["team_energy"])
        game["cash"] = max(0, game["cash"])
        game["bug_count"] = max(0, game["bug_count"])
        game["caffeine"] = max(0, game["caffeine"])
        game["market_traction"] = max(0, game["market_traction"])
        game["travel_progress"] = min(100, max(0, game["travel_progress"]))
    

        game["current_location"] = get_location_from_progress(game["travel_progress"])

        return game


    def _apply_event_effects_to_user(self, game: Game, event: EventType, player_choice: EventChoice):
        event_data = GAME_EVENTS[event]
        choice_data = event_data["effects"][player_choice]

        if "random_outcomes" in choice_data:
            outcome = get_hackathon_outcome()
            effects = choice_data["random_outcomes"][outcome]
        else:
            effects = choice_data

        game.team_energy += effects["team_energy"]
        game.cash += effects["cash"]
        game.bug_count += effects["bug_count"]
        game.caffeine += effects["caffeine"]
        game.market_traction += effects["market_traction"]

        game.team_energy = max(0, game.team_energy)
        game.cash = max(0, game.cash)
        game.bug_count = max(0, game.bug_count)
        game.caffeine = max(0, game.caffeine)
        game.market_traction = max(0, game.market_traction)

        return game


    def _apply_event_effects_to_guest(self, game: dict, event: EventType, player_choice : EventChoice):

        event_data = GAME_EVENTS[event]
        choice_data = event_data["effects"][player_choice]

        if "random_outcomes" in choice_data:
            outcome = get_hackathon_outcome()
            effects = choice_data["random_outcomes"][outcome]
        else:
            effects = choice_data
        
        game["team_energy"] += effects["team_energy"]
        game["cash"] += effects["cash"]
        game["bug_count"] += effects["bug_count"]
        game["caffeine"] += effects["caffeine"]
        game["market_traction"] += effects["market_traction"]

        game["team_energy"] = max(0, game["team_energy"])
        game["cash"] = max(0, game["cash"])
        game["bug_count"] = max(0, game["bug_count"])
        game["caffeine"] = max(0, game["caffeine"])
        game["market_traction"] = max(0, game["market_traction"])

        return game

    def _apply_weather_effect_user(self, game: Game, weather: Weather):
        effect = get_weather_effect(weather.temperature)

        game.team_energy+=effect["energy"]
        game.caffeine+=effect["coffee"]

        return  effect["description"]
    

    def _apply_weather_effect_to_guest(self, game: dict, weather: Weather):
        effect = get_weather_effect(weather.temperature)

        game["team_energy"]+=effect["energy"]
        game["caffeine"]+=effect["coffee"]

        return  effect["description"]

    def _apply_traffic_effect_user(self, game: Game, data_traffic: DataTraffic):
        effect = get_traffic_effect(data_traffic)

        game.team_energy+=effect["energy"]
        game.caffeine+= effect["coffee"]

        return effect["description"]



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
    


    async def apply_action_by_id(self, game_id: int, action: GameAction, user: User) -> dict:
        game = await self.session.get(Game, game_id)

        if not game:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Game not found"
            )

        if game.user_id != user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized"
            )

        return await self.apply_action(game, action)
    

    async def apply_action(self, game: Game, action: GameAction )-> dict:

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

        triggered_event = None
        event_response = None
        weather_description = None
        traffic_description = None

        if game.status == GameStatus.in_progress:
            location_coordinates = get_coordinates_from_location(game.current_location)
            weather = await get_weather(location_coordinates)

            weather_description  = self._apply_weather_effect_user(game, weather)

            game.status= get_game_status(
                game.travel_progress,
                game.team_energy
            )
        
        if game.status == GameStatus.in_progress:

            current_milestone = get_milestone_by_location(game.current_location)
            next_location = current_milestone["next_location"]

            if next_location is not None:
                origin = get_coordinates_from_location(game.current_location)
                destination = get_coordinates_from_location(next_location)


                traffic = await get_traffic(origin, destination, game.current_location)

                traffic_description = self._apply_traffic_effect_user(game,traffic)
                
                game.status= get_game_status(
                    game.travel_progress,
                    game.team_energy
                )

        if game.status == GameStatus.in_progress:
            triggered_event = maybe_get_event(action)

            if triggered_event:
                event_data = GAME_EVENTS[triggered_event]

                event_response = {
                    "event_type": triggered_event,
                    "title": event_data["title"],
                    "description": event_data["description"],
                    "choices": event_data["choices"]
                }

        
        try:
            await self.session.commit()
            await self.session.refresh(game)
            
            return {
                "game": game,
                "event":event_response,
                "weather_description": weather_description,
                "traffic_description": traffic_description
            }
        
        except SQLAlchemyError:
            await self.session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Could not apply action"
            )
    

    async def apply_action_to_guest(self, game: dict, action: GameAction ) -> dict:

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

        triggered_event = None
        event_response = None
        weather_description = None
        if game["status"] == GameStatus.in_progress:
            location_coordinates = get_coordinates_from_location(game["current_location"])
            weather = await get_weather(location_coordinates)

            weather_description  = self._apply_weather_effect_to_guest(game, weather)

            game["status"]= get_game_status(
                game["travel_progress"],
                game["team_energy"]
            )

            if game["status"] == GameStatus.in_progress:
                triggered_event = maybe_get_event(action)
        
                if triggered_event:
                    event_data = GAME_EVENTS[triggered_event]
                    event_response = {
                        "event_type": triggered_event,
                        "title": event_data["title"],
                        "description": event_data["description"],
                        "choices": event_data["choices"]
                    }
        
        return {
                "game":game,
                "event":event_response,
                "weather_description": weather_description
        }
    
    


    
    async def apply_event_to_user(self, game: Game, event:EventType, player_choice: EventChoice)-> Game:

        if game.status != GameStatus.in_progress:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Game is already finished"
            )

        self._apply_event_effects_to_user(game, event, player_choice)

        game.status = get_game_status(
            game.travel_progress,
            game.team_energy
        )

        event_record = GameEvent(
            game_id=game.id,
            event_type=event,
            player_choice=player_choice,
            day=game.current_day,
            description=""
        )

        self.session.add(event_record)

        try:
            await self.session.commit()
            await self.session.refresh(game)
            return game
        except SQLAlchemyError:
            await self.session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Could not apply event"
            )
        


        
    def apply_event_to_guest(self, game: dict, event: EventType, player_choice: EventChoice ) -> dict:

        if game["status"] != GameStatus.in_progress:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Game is already finished"
            )
        
        self._apply_event_effects_to_guest(game,event,player_choice)
        
        game["status"]= get_game_status(
            game["travel_progress"],
            game["team_energy"]
        )
        
        return game
    

    async def apply_event_by_id( self, game_id: int, event: EventType, player_choice: EventChoice, user: User) -> Game:
        game = await self.session.get(Game, game_id)

        if not game:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Game not found"
            )
        if game.user_id != user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized"
            )
        
        return await self.apply_event_to_user(game, event, player_choice)
    
    async def save_game(self, game_id: int, user: User)->Game:
        game = await self.session.get(Game, game_id)
        if not game:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Game not found"
            )
        if game.user_id != user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized"
            )
        if game.status != GameStatus.in_progress:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only in-progress games can be saved"
            )

        game.status = GameStatus.saved

        try:
            await self.session.commit()
            await self.session.refresh(game)
            return game

        except SQLAlchemyError:
            await self.session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Could not save game"
            )
