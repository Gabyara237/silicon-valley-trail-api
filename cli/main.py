
from cli.display import display_option_title, display_rules
from cli.handlers import handle_login, handle_play_as_guest, handle_quit, handle_register
from cli.menus import welcome_menu


def run():
    while True:
        choice = welcome_menu()

        if choice == 1:
            display_option_title("Login")
            handle_login()

        elif choice == 2:
            display_option_title("Register")
            handle_register()

        elif choice == 3:
            display_option_title("Play as Guest")
            game = handle_play_as_guest()

            if game:
                print("Starting game...")

        elif choice == 4:
            display_rules()

        elif choice == 5:
            handle_quit()


if __name__ == "__main__":
    run()