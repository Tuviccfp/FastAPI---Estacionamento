from typing import Annotated
from fastapi import Path
from fastapi import APIRouter, Depends
from user.user_table import UserTable, UserEmailDTO
from user.user_controller import UserControllerDep

router_user = APIRouter()

@router_user.post("/get-by-email")
async def get_user_by_email(user: UserEmailDTO, controller: UserControllerDep):
    check_user = await controller.get_user_controller(user.email)
    return check_user

@router_user.post("/new-user")
async def new_user(user: UserTable, controller: UserControllerDep) -> str:
    await controller.create_controller(user)
    return "Usuário criado com sucesso"