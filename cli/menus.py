
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
            choice = int(input("\nEnter your choice (1-4): "))
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
            continue

        if is_valid(choice,1,5):
            return choice
        
        print("\nInvalid option. Please choose a number between 1 and 4.\n")