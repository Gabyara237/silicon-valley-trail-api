
from cli.utils import is_valid


def welcome_menu():
    while True:
        print("\n====================================")
        print("     🚀 Silicon Valley Trail 🚀")
        print("====================================\n\n")
        print("1) Login")
        print("2) Register")
        print("3) Play as Guest")
        print("4) View Rules")
        print("5) Quit")
        
        try:
            choice = int(input("\nEnter your choice (1-5): "))
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
            continue

        if is_valid(choice,1,5):
            return choice
        
        print("\nInvalid option. Please choose a number between 1 and 5.\n")


def post_login_menu_with_active_game():
    while True:
        print("\n====================================")
        print("        🎮 Game Menu 🎮")
        print("====================================\n")
        print("1) Resume Game")
        print("2) Start New Game")
        print("3) Logout")

        try:
            choice = int(input("\nEnter your choice (1-3): "))
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
            continue

        if is_valid(choice, 1, 3):
            return choice

        print("\nInvalid option. Please choose a number between 1 and 3.\n")



def post_login_menu_no_active_game():
    while True:
        print("\n====================================")
        print("        🎮 Game Menu 🎮")
        print("====================================\n")
        print("1) Start New Game")
        print("2) Logout")

        try:
            choice = int(input("\nEnter your choice (1-2): "))
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
            continue

        if is_valid(choice, 1, 2):
            return choice

        print("\nInvalid option. Please choose a number between 1 and 2.\n")