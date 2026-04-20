
import asyncio

from cli.api_client import abandon_game_request, apply_event_request, apply_guest_event_request, get_ai_advice_request, perform_game_action_request, perform_guest_action_request, save_game_request
from cli.display import display_action_feedback, display_action_selected_message
from cli.menus import event_choice_menu
from cli.prompts import prompt_confirm_abandon


def handle_game_action(game: dict, action: str, token: str):
    game_id = game.get("id")

    display_action_selected_message(action)
    
    response = asyncio.run(perform_game_action_request(game_id, action, token))

    if response.status_code == 200:
        result = response.json()

        updated_game = result.get("game")

        event = result.get("event")

        display_action_feedback(result)

        if event:
            updated_game = handle_event(updated_game, event, token)

        return updated_game


    print("\nFailed to apply action.")
    try:
        print(response.json())
    except Exception:
        print(response.text)

    return game



def handle_event(game: dict, event: dict, token: str):
    game_id = game.get("id")
    event_type = event.get("event_type")

    player_choice = event_choice_menu(event)

    response = asyncio.run(apply_event_request(game_id, event_type, player_choice, token))

    if response.status_code == 200:
        updated_game = response.json()
        print(f"\n You chose: {player_choice.capitalize()}\n")
        return updated_game

    print("\nFailed to apply event choice.")
    try:
        print(response.json())
    except Exception:
        print(response.text)

    return game


def handle_save_game(game: dict, token: str):
    game_id = game.get("id")

    print("\n💾 Saving game...\n")

    response = asyncio.run(save_game_request(game_id, token))

    if response.status_code == 200:
        print("✅ Game saved successfully!\n")
        input("Press Enter to return to the menu...")
        return True 

    print("\nFailed to save game.")
    try:
        print(response.json())
    except Exception:
        print(response.text)

    return False


def handle_abandon_game(game: dict, token: str):
    confirm = prompt_confirm_abandon()

    if not confirm:
        print("\nAbandon cancelled.\n")
        return False

    game_id = game.get("id")

    print("\nAbandoning game...\n")

    response = asyncio.run(abandon_game_request(game_id, token))

    if response.status_code == 200:
        print("✅ Game abandoned successfully.\n")
        input("Press Enter to return to the menu...")
        return True

    print("\nFailed to abandon game.")
    try:
        print(response.json())
    except Exception:
        print(response.text)

    return False


def handle_ai_advice(game: dict, token: str):
    game_id = game.get("id")

    print("\n🤖 Asking your AI startup advisor...\n")

    try:
        response = asyncio.run(get_ai_advice_request(game_id, token))
    except Exception as e:
        print("==================================================")
        print("🤖 AI STRATEGY ADVICE")
        print("--------------------------------------------------")
        print("AI advice is temporarily unavailable. Try again in a moment.")
        print("==================================================\n")
        input("Press Enter to continue...")
        return

    if response.status_code == 200:
        data = response.json()
        advice = data.get("advice")

        print("==================================================")
        print("🤖 AI STRATEGY ADVICE")
        print("--------------------------------------------------")
        print(advice)
        print("==================================================\n")
        input("Press Enter to continue...")
        return

    print("\nFailed to get AI advice.")
    try:
        print(response.json())
    except Exception:
        print(response.text)

def handle_guest_event(game: dict, event: dict):
    player_choice = event_choice_menu(event)
    event_type = event.get("event_type")

    response = asyncio.run(
        apply_guest_event_request(game, event_type, player_choice)
    )

    if response.status_code == 200:
        updated_game = response.json()
        print(f"\nYou chose: {player_choice.capitalize()}\n")
        return updated_game

    print("\nFailed to apply guest event choice.")
    try:
        print(response.json())
    except Exception:
        print(response.text)

    return game


def handle_guest_game_action(game: dict, action: str):
    display_action_selected_message(action)

    response = asyncio.run(perform_guest_action_request(game, action))

    if response.status_code == 200:
        result = response.json()

        updated_game = result.get("game")
        event = result.get("event")

        display_action_feedback(result)

        if event:
            updated_game = handle_guest_event(updated_game, event)

        return updated_game

    print("\nFailed to apply guest action.")
    try:
        print(response.json())
    except Exception:
        print(response.text)

    return game


def handle_guest_abandon_game():
    confirm = prompt_confirm_abandon()

    if not confirm:
        print("\nAbandon cancelled.\n")
        return False

    print("\nGuest game abandoned.\n")
    input("Press Enter to return to the main menu...")
    return True