from fastapi import Depends, HTTPException
from typing import Annotated

from database.sql_connect import SessionDep
from user.user_repository import UserRepository
from user.user_service import UserService
from user.user_table import UserTable, UserDTOUpdate, UserReduce


class UserController:
    def __init__(self, service: UserService):
        self.service = service

    async def create_controller(self, user: UserTable):
        return await self.service.create_new_user(user)

    async def user_login(self, email: str, password: str):
        return await self.service.user_login(email, password)

    async def get_all_users(self) -> list[UserTable]:
        result = await self.service.get_all_users()
        return result

    async def get_user_by_id(self, user_id: int | None) -> UserReduce:
        user = await self.service.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Erro ao localizar usuário")
        return UserReduce(id=user.id, email=user.email, nome=user.nome, role=user.role)

    async def delete_user_by_id(self, user_id: int) -> str:
        user = await self.service.delete_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return "Usuário deletado com sucesso"

    async def update_user(self, user_id: int, user: UserTable) -> UserReduce:
        await self.service.update_user(user_id, user)
        return await self.get_user_by_id(user_id)

def get_user_controller(db: SessionDep):
    repo = UserRepository(db)
    service = UserService(repo)
    return UserController(service)

UserControllerDep = Annotated[UserController, Depends(get_user_controller)]