from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import HTTPException, status
from pwdlib import PasswordHash
import jwt

from app.config import security_settings


password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None)->str:

    
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(hours=1)

    token = jwt.encode(
        payload={
            "sub": data["username"],
            "email": data["email"],
            "exp": expire
        },
        algorithm=security_settings.JWT_ALGORITHM,
        key=security_settings.JWT_SECRET,
    )

    return token


def decode_access_token(token: str)-> dict:
    try:
        payload = jwt.decode(
            jwt=token,
            key= security_settings.JWT_SECRET,
            algorithms=[security_settings.JWT_ALGORITHM]
        )
        return payload
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
    
        )
    
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid token"
        )
    

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/sign-in")