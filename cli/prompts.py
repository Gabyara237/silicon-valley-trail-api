
from cli.utils import is_email_valid


def prompt_email():
    while True:
        email = input("Enter your email: ").strip().lower()
        
        if is_email_valid(email):
            return email
        
        print("Invalid email format. Try again.\n")


def prompt_password():
    while True:
        password = input("Enter your password: ").strip()

        if len(password)>=6:
            return password

        print("Password must be at least 6 characters.\n")


def prompt_username():
    while True:
        username = input("Enter your username: ").strip().lower()

        if len(username)>=3:
            return username
        
        print("Username must be at least 3 characters.\n")

def prompt_confirm_abandon():
    print("\n==================================================")
    print("🚨 ABANDON YOUR STARTUP?")
    print("==================================================\n")
    print("This decision cannot be undone.\n")

    while True:
        choice = input("Do you really want to abandon your startup? (y/n): ").strip().lower()

        if choice in ("y", "n"):
            return choice == "y"

        print("Invalid input. Please enter 'y' or 'n'.\n")
