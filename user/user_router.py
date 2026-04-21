from typing import Annotated
from fastapi import Path
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from middleware.auth.auth import CurrentUser
from user.user_table import UserTable, UserEmailDTO, UserReduce
from user.user_controller import UserControllerDep

router_user = APIRouter()

@router_user.post("/new-user")
async def new_user(user: UserTable, controller: UserControllerDep) -> UserReduce:
    user = await controller.create_controller(user)
    return UserReduce(id=user.id, email=user.email, nome=user.nome, role=user.role)

@router_user.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], controller: UserControllerDep):
    return await controller.user_login(form_data.username, form_data.password)

@router_user.get("/me")
async def get_user_by_id(current_user: CurrentUser):
    return current_user