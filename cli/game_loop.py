

from cli.display import display_game_intro, display_game_over, display_game_status, display_victory
from cli.game_handlers import handle_game_action, handle_save_game
from cli.menus import game_menu


def handle_endgame(game: dict):
    status = game.get("status")

    if status == "won":
        display_victory(game)
        return True

    if status == "lost":
        display_game_over(game)
        return True

    return False

def game_loop(game: dict, token: str, is_new_game: bool = False):
    if is_new_game:
        display_game_intro()

    while True:
        display_game_status(game)

        choice = game_menu()

        if choice == 1:
            game = handle_game_action(game, "rest", token)
            if handle_endgame(game):
                return
        elif choice == 2:
            game = handle_game_action(game, "work_on_product", token)
            if handle_endgame(game):
                return
        elif choice == 3:
            game = handle_game_action(game, "marketing_push", token)
            if handle_endgame(game):
                return
        elif choice == 4:
            game = handle_game_action(game, "travel", token)
            if handle_endgame(game):
                return
        elif choice == 5:
            game = handle_game_action(game, "buy_coffee", token)
            if handle_endgame(game):
                return
        elif choice == 6:
            should_exit = handle_save_game(game, token)
            if should_exit:
                return
        elif choice == 7:
            print("\n Abandon Game selected (coming soon)")
        elif choice == 8:
            print("\nReturning to main menu...\n")
            return