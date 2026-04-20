from fastapi import Depends
from typing import Annotated

from database.sql_connect import SessionDep
from user.user_repository import UserRepository
from user.user_service import UserService
from user.user_table import UserTable


class UserController:
    def __init__(self, service: UserService):
        self.service = service

    async def create_controller(self, user: UserTable):
        return await self.service.create_new_user(user)

    async def user_login(self, email: str, password: str):
        return await self.service.user_login(email, password)

    async def get_user_by_id(self, user_id: int):
        return await self.service.get_by_id(user_id)

def get_user_controller(db: SessionDep):
    repo = UserRepository(db)
    service = UserService(repo)
    return UserController(service)

UserControllerDep = Annotated[UserController, Depends(get_user_controller)]