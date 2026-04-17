from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app.core.security import decode_access_token, oauth2_scheme
from app.models.user import User
from sqlalchemy import select

from fastapi import Depends, HTTPException,status
from app.database.session import get_session
from app.services.user import UserService
from app.services.auth import AuthService

SessionDep = Annotated[AsyncSession, Depends(get_session)]


def get_user_service(session: SessionDep):
    return UserService(session)

UserServiceDep = Annotated[ 
    UserService, 
    Depends(get_user_service)
]


def get_auth_service(session: SessionDep):
    return AuthService(session)

AuthServiceDep = Annotated[
    AuthService,
    Depends(get_auth_service)
]


async def get_current_user(session: SessionDep, token: str = Depends(oauth2_scheme))-> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credentials could not be validated",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(token)
    user_id = payload.get("sub")

    if user_id is None:
        raise credentials_exception

    result = await session.execute(
        select(User).where(User.id == int(user_id))
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise credentials_exception

    return user

CurrentUserDep = Annotated[
    User, Depends(get_current_user)
]