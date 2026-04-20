
from cli.utils import is_valid


def welcome_menu():
    while True:
        print("\n==============================================")
        print("     🚀 Welcome to Silicon Valley Trail 🚀")
        print("================================================\n\n")
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

def game_menu():
    while True:
        print("\n==================================================")
        print("                 What will you do?")
        print("==================================================\n")
        print("1) Rest              - Restore team energy, but use caffeine")
        print("2) Work on Product   - Improve the product, reduce bugs, and spend energy")
        print("3) Marketing Push    - Boost traction, but costs cash")
        print("4) Travel            - Move forward, but traffic and weather may affect you")
        print("5) Buy Coffee        - Restore caffeine, but costs cash")
        print("6) Get AI Advice     - Ask for the best strategic next move")
        print("7) Save Game         - Save your current progress")
        print("8) Abandon Game      - Give up this run")
        print("9) Back              - Return to the previous menu\n")

        try:
            choice = int(input("Choose your action (1-9): "))
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
            continue

        if is_valid(choice, 1, 9):
            return choice

        print("\nInvalid option. Please choose a number between 1 and 9.\n")


def event_choice_menu(event: dict):
    choices = event.get("choices", [])

    while True:
        print("\n🎲 RANDOM EVENT")
        print("==================================================")
        print(f"📌 {event.get('title')}\n")
        print(f"  {event.get("description")}\n")

        for index, choice in enumerate(choices, start=1):
            print(f"{index}) {choice.capitalize()}")

        try:
            user_choice = int(input(f"\nChoose an option (1-{len(choices)}): "))
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
            continue

        if 1 <= user_choice <= len(choices):
            return choices[user_choice - 1]

        print(f"\nInvalid option. Please choose a number between 1 and {len(choices)}.\n")