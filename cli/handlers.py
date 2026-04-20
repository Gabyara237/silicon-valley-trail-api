import asyncio
from cli.prompts import prompt_email, prompt_password, prompt_username
from cli.api_client import login_request, register_request

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
