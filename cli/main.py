
from cli.display import display_option_title
from cli.handlers import handle_login, handle_register
from cli.menus import welcome_menu


def run():
    choice = welcome_menu()

    if choice == 1:
        display_option_title("Login")
        handle_login()

    elif choice == 2:
        display_option_title("Login")
        handle_register()
        
    elif choice == 3:
        print("Play as Guest selected")
    elif choice == 4:
        print("View Rules selected")

if __name__ == "__main__":
    run()