import asyncio
from app.database.session import create_db_tables

async def init():
    await create_db_tables()

asyncio.run(init())