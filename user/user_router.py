from typing import Annotated
from fastapi import Path
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from middleware.auth.auth import CurrentUser
from user.user_table import UserTable, UserEmailDTO, UserReduce, UserDTOUpdate
from user.user_controller import UserControllerDep

router_user = APIRouter()

@router_user.post("/new-user")
async def new_user(user: UserTable, controller: UserControllerDep) -> UserReduce:
    user = await controller.create_controller(user)
    return UserReduce(id=user.id, email=user.email, nome=user.nome, role=user.role)

@router_user.get("/get-all-users")
async def get_all_users(controller: UserControllerDep, current_user: CurrentUser):
    return await controller.get_all_users()

@router_user.get("/get-user-by-id/{user_id}")
async def get_user_by_id(user_id: int | None, controller: UserControllerDep, current_user: CurrentUser):
    return await controller.get_user_by_id(user_id)

@router_user.delete("/delete-user-by-id/{user_id}")
async def delete_user_by_id(user_id: int, controller: UserControllerDep, current_user: CurrentUser):
    return await controller.delete_user_by_id(user_id)

@router_user.put("/update-user/{user_id}")
async def update_user(user_id: int, user: UserTable, controller: UserControllerDep, current_user: CurrentUser):
    print(user_id, user)
    return await controller.update_user(user_id, user)

@router_user.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], controller: UserControllerDep):
    return await controller.user_login(form_data.username, form_data.password)

@router_user.get("/me")
async def get_current_user(current_user: CurrentUser):
    return current_user

