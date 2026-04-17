from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from fastapi import Depends
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