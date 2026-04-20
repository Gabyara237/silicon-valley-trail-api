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