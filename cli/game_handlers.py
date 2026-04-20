
import asyncio

from cli.api_client import perform_game_action_request
from cli.display import display_action_feedback, display_action_selected_message


def handle_game_action(game: dict, action: str, token: str):
    game_id = game.get("id")

    display_action_selected_message(action)
    
    response = asyncio.run(perform_game_action_request(game_id, action, token))

    if response.status_code == 200:
        result = response.json()

        updated_game = result.get("game")

        display_action_feedback(result)
        
        return updated_game

    print("\nFailed to apply action.")
    try:
        print(response.json())
    except Exception:
        print(response.text)

    return game