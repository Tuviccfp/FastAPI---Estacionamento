from datetime import timedelta
from typing import Annotated

from fastapi import HTTPException, Depends
from pygments.lexers import pascal
from sqlalchemy.ext.asyncio import AsyncSession

from middleware.auth.token import create_access_token, Token
from user.user_repository import UserRepository
from user.user_table import UserTable, UserReduce, UserDTOUpdate
from utils.hash import verify_password, create_hash

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def __get_by_email(self, email: str):
        return await self.user_repo.get_by_email(email)

    async def __authenticate_user(self, email: str, password: str) -> UserTable:
        user = await self.__get_by_email(email)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário inexistente")
        if not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
        return user

    async def create_new_user(self, user: UserTable):
        get_email = await self.__get_by_email(user.email)
        if get_email:
            raise HTTPException(status_code=409, detail="E-mail já existe")
        new_user: UserTable = UserTable(
            nome=user.nome,
            email=user.email,
            password=create_hash(user.password),
            role=user.role
        )
        await self.user_repo.create(new_user)
        return UserReduce(id=new_user.id, email=new_user.email, nome=new_user.nome, role=new_user.role)

    async def user_login(self, email: str, password: str):
        user = await self.__authenticate_user(email, password)
        if not user:
            raise HTTPException(status_code=401, detail="")
        acess_expires_token = timedelta(minutes=30)
        create_token = create_access_token(data={"id": user.id, "role": user.role}, expires_delta=acess_expires_token)
        return Token(acess_token=create_token, token_type="bearer")

    async def get_all_users(self):
        users = await self.user_repo.get_all()
        return [UserReduce(id=user.id, email=user.email, nome=user.nome, role=user.role) for user in users]

    async def get_by_id(self, user_id: int | None):
        user = await self.user_repo.get_by_id(user_id)
        return user

    async def delete_by_id(self, user_id: int):
        return await self.user_repo.delete_by_id(user_id)

    async def update_user(self, user_id: int, user: UserTable):
        user: UserTable = UserTable(
            id=user_id,
            nome=user.nome,
            email=user.email,
            password=create_hash(user.password),
            role=user.role
        )
        return await self.user_repo.update_user(user_id, user)

def get_user_service(db: AsyncSession):
    repo = UserRepository(db)
    return UserService(repo)

UserServiceDep = Annotated[UserService, Depends(get_user_service)]