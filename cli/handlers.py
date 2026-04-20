import asyncio
from cli.prompts import prompt_email, prompt_password, prompt_username
from cli.api_client import login_request, play_as_guest_request, register_request

def handle_login():
    email = prompt_email()
    password = prompt_password()

    response = asyncio.run(login_request(email, password))

    if response.status_code == 200:
        data = response.json()
        print("\nLogin successful!")
        print(f"\nAccess token: {data['access_token']}\n")
    else:
        print("\n Login failed")
        print(response.json())


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
    print(response.json())
    return None
