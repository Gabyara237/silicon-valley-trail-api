from fastapi import FastAPI 
from app.routes.auth import router as auth_router
from app.routes.game import router as game_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(game_router)

@app.get("/")
def welcome():
    return "Hello world"