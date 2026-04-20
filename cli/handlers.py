import asyncio
from cli.display import display_option_title
from cli.game_loop import game_loop
from cli.menus import  post_login_menu_no_active_game, post_login_menu_with_active_game
from cli.prompts import prompt_email, prompt_password, prompt_username
from cli.api_client import  create_new_game_request, get_active_game_request, login_request, play_as_guest_request, register_request

def handle_login():
    email = prompt_email()
    password = prompt_password()

    response = asyncio.run(login_request(email, password))

    if response.status_code == 200:
        data = response.json()
        token = data["access_token"]

        print("\n✅ Login successful!\n")

        handle_post_login_menu(token)
    else:
        print("\n Login failed")
        try:
            print(response.json())
        except Exception:
            print(response.text)


def handle_register():
    username = prompt_username()
    email =prompt_email()
    password = prompt_password()
    
    response = asyncio.run(register_request(username,email,password))

    if response.status_code == 201:
        print("\nRegistration successful!\n")
    else:
        print("\nRegistration failed")
        print(response.json())


def handle_play_as_guest():
    username = prompt_username()

    response = asyncio.run(play_as_guest_request(username))

    if response.status_code == 200:
        game = response.json()
        print("\nGuest game created successfully!\n")
        return game

    print("\nFailed to create guest game.\n")
    try:
        print(response.json())
    except Exception:
        print(response.text)
    return None


def handle_quit():
    print("\nThanks for playing Silicon Valley Trail. Goodbye!\n")
    raise SystemExit



def handle_post_login_menu(token: str):
    response = asyncio.run(get_active_game_request(token))

    if response.status_code != 200:
        print("\n Failed to retrieve active game.")
        try:
            print(response.json())
        except Exception:
            print(response.text)
        return

    data = response.json()
    active_game = data.get("active_game")

    if active_game is None:
        choice = post_login_menu_no_active_game()

        if choice == 1:
            display_option_title("Start New Game")
            game = handle_start_new_game(token)
        elif choice == 2:
            print("\nLogout selected")

    else:
        choice = post_login_menu_with_active_game()

        if choice == 1:
            print("\nResume Game selected")
        elif choice == 2:
            display_option_title("Start New Game")
            game = handle_start_new_game(token)
            if game:
                game_loop(game, token, True)
        elif choice == 3:
            print("\nLogout selected")


def handle_start_new_game(token: str):
    response= asyncio.run(create_new_game_request(token))

    if response.status_code == 200:
        game = response.json()
        print("\nUser game created successfully!\n")
        return game
    
    print("\nFailed to create new game.\n")
    try:
        print(response.json())
    except Exception:
        print(response.text)
    return None




