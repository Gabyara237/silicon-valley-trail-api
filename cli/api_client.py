import httpx


BASE_URL="http://127.0.0.1:8000"

async def login_request(email,password):

    data = {
        "username": email,
        "password": password
    }    

    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/auth/sign-in"
        response = await client.post(url,data=data)
        return response
    

async def register_request(username,email,password):
    data ={
        "username": username,
        "email":email,
        "password": password
    }
    
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/auth/sign-up"
        response = await client.post(url,json=data)
        return response

async def play_as_guest_request(username):
    data ={
        "guest_username": username
    }

    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/games/guest"
        response = await client.post(url,json=data)
        return response
    

async def get_active_game_request(token: str):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/games/active"
        response = await client.get(url, headers=headers)
        return response