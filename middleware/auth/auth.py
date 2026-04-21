from typing import Annotated

import jwt
from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError

from middleware.auth.token import SECRET_KEY, ALGORITHM
from user.user_controller import UserControllerDep

from user.user_table import UserTable

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], controller: UserControllerDep):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int | None = payload.get("id")
        role: str = payload.get("role")
        if id is None and role is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = await controller.get_user_by_id(id)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

CurrentUser = Annotated[UserTable, Depends(get_current_user)]