

from cli.display import display_game_intro, display_game_status
from cli.menus import game_menu


def game_loop(game: dict, token: str, is_new_game: bool = False):
    if is_new_game:
        display_game_intro()

    while True:
        display_game_status(game)

        choice = game_menu()

        if choice == 1:
            print("\n Rest selected ")
        elif choice == 2:
            print("\n Work on Product selected ")
        elif choice == 3:
            print("\n Marketing Push selected ")
        elif choice == 4:
            print("\n Travel selected ")
        elif choice == 5:
            print("\n Save Game selected ")
        elif choice == 6:
            print("\n Abandon Game selected (coming soon)")
        elif choice == 7:
            print("\nReturning to main menu...\n")
            return