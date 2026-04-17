from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.core.security import verify_password, create_access_token

class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def login(self, email, password) -> str:
        normalized_email = email.lower().strip()

        result = await self.session.execute(
            select(User).where(User.email == normalized_email)
        )

        user = result.scalar()

        if user is None or not verify_password(
            password,
            user.hashed_password,
        ):
            raise HTTPException(
                status_code= status.HTTP_401_UNAUTHORIZED,
                detail= "Email or password is incorrect",
            )


        token = create_access_token({"user_id":user.id,"email": normalized_email})
        
        return token

