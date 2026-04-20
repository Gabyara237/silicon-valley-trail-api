
from cli.utils import is_valid

def welcome_menu():
    while True:
        print("====================================")
        print("     🚀 Silicon Valley Trail 🚀")
        print("====================================")
        print("1) Login")
        print("2) Register")
        print("3) Play as Guest")
        print("4) View Rules")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
            continue

        if is_valid(choice,1,4):
            return choice
        
        print("\nInvalid option. Please choose a number between 1 and 4.\n")

