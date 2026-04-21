from datetime import datetime, timezone, timedelta
from typing import Annotated

import jwt

from pydantic import BaseModel

ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = "a76a6785af3bf717a8f107b963fecb9f6a62d36500efc7dc0c415baa3484f3a0"
ALGORITHM = "HS256"

class Token(BaseModel):
    acess_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None
    role: str | None = None

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
