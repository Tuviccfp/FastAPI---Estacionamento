from fastapi import APIRouter, Depends
from user.user_table import UserTable
from user.user_controller import UserControllerDep

router_user = APIRouter()

@router_user.get("/get-by-email/{email}")
def get_user_by_email(email: str, controller: UserControllerDep):
    check_user = controller.get_user_controller(email)
    return check_user

@router_user.post("/new-user")
async def new_user(user: UserTable, controller: UserControllerDep) -> UserTable:
    result = controller.create_controller(user)
    return result