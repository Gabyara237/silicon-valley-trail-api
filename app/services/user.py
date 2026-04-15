from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException,status

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password



class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create_user(self, credentials: UserCreate) -> User:
        
        normalized_username = credentials.username.lower().strip()
        normalized_email = credentials.email.lower().strip()
        
        hashed_password=hash_password(credentials.password)
        
        user = User(
            username= normalized_username,
            email= normalized_email,
            hashed_password=hashed_password,
        )

        self.session.add(user)

        try:
            await self.session.commit()
            await self.session.refresh(user)
            return user
        
        except IntegrityError:
            await self.session.rollback()

            raise HTTPException(
                status_code= status.HTTP_409_CONFLICT,
                detail="Username or email already exists"
            )

