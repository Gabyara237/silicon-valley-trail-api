
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
