from datetime import datetime, timezone
from sqlalchemy import Column, DateTime
from typing import Optional
from sqlmodel import SQLModel,Field


class User(SQLModel, table=True):

    __tablename__= "users"
    
    id: Optional[int] = Field(default=None,primary_key=True)
    username: str = Field(max_length=50, index=True, unique=True, nullable=False)
    email: str = Field(max_length=255, index=True, unique=True, nullable=False)
    hashed_password: str = Field(max_length=255, nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True)), default_factory=lambda: datetime.now(timezone.utc))