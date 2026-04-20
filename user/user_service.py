from fastapi import HTTPException
from pwdlib import PasswordHash
from pygments.lexers import pascal

from user.user_repository import UserRepository
from user.user_table import UserTable
from utils.hash import verify_password, create_hash


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def __get_by_email(self, email: str):
        return await self.user_repo.get_by_email(email)

    async def __authenticate_user(self, email: str, password: str):
        user = await self.__get_by_email(email)
        if not user:
            verify_password(password, user.password)
            return False
        if not verify_password(password, user.password):
            return False
        return user

    async def create_new_user(self, user: UserTable):
        get_email = self.__get_by_email(user.email)
        if await get_email:
            raise HTTPException(status_code=409, detail="E-mail já existe")
        new_user: UserTable = UserTable(
            nome=user.nome,
            email=user.email,
            password=create_hash(user.password),
        )
        return await self.user_repo.create(new_user)

    async def get_by_id(self, user_id: int):
        return await self.user_repo.get_by_id(user_id)

    # async def user_login(self, ):

