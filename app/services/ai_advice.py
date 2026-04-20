from app.integrations.ai_client import AIClient
from app.models.game import Game

FALLBACK_ADVICE = (
    "Focus on your weakest resource first. "
    "If energy is low, rest. If caffeine is low, buy coffee. "
    "If cash is low, avoid expensive actions."
)


class AIAdviceService:
    def __init__(self):
        self.ai_client = AIClient()

    def build_prompt(self, game: Game) -> str:
        return (f"""
            You are a strategic startup advisor inside a simulation game called Silicon Valley Trail.

            Your role:
            - Give the player short, practical advice based on the current game state.
            - Recommend the SINGLE best next action from this list only:
            rest, work_on_product, marketing_push, travel, buy_coffee

            Game context:
            - The player is trying to travel from San Jose to San Francisco for a final pitch.
            - If team energy reaches 0, the player loses.
            - If cash reaches 0, the player loses.
            - If travel progress reaches 100, the player wins.

            Current game state:
            - Day: {game.current_day}
            - Location: {game.current_location}
            - Cash: {game.cash}
            - Team Energy: {game.team_energy}
            - Caffeine: {game.caffeine}
            - Market Traction: {game.market_traction}
            - Bug Count: {game.bug_count}
            - Travel Progress: {game.travel_progress}
            - Status: {game.status}

            Instructions:
            - Keep the answer under 3 short sentences.
            - Be clear and practical.
            - Mention the recommended action explicitly.
            - Briefly explain why.
            - Do not invent game mechanics.
            """)

    def get_advice(self, game: Game) -> str:
        prompt = self.build_prompt(game)
        advice = self.ai_client.generate_strategy_advice(prompt)

        if advice:
            return advice

        return FALLBACK_ADVICE