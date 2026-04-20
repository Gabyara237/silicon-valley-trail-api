

from cli.display import display_game_intro, display_game_status
from cli.game_handlers import handle_game_action
from cli.menus import game_menu


def game_loop(game: dict, token: str, is_new_game: bool = False):
    if is_new_game:
        display_game_intro()

    while True:
        display_game_status(game)

        choice = game_menu()

        if choice == 1:
            game = handle_game_action(game, "rest", token)
        elif choice == 2:
            game = handle_game_action(game, "work_on_product", token)
        elif choice == 3:
            game = handle_game_action(game, "marketing_push", token)
        elif choice == 4:
            game = handle_game_action(game, "travel", token)
        elif choice == 5:
            print("\n Save Game selected ")
        elif choice == 6:
            print("\n Abandon Game selected (coming soon)")
        elif choice == 7:
            print("\nReturning to main menu...\n")
            return