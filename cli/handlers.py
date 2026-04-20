import asyncio
from cli.prompts import prompt_email, prompt_password
from cli.api_client import login_request

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