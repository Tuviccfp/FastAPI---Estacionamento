from typing import Tuple

from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session, select

from user.user_table import UserTable, UserReduce


class UserRepository:
    def __init__(self, db_table: AsyncSession):
        self.db_table = db_table

    async def create(self, user: UserTable):
        self.db_table.add(user)
        await self.db_table.commit()
        await self.db_table.refresh(user)
        return UserReduce(id=user.id, email=user.email, nome=user.nome, role=user.role)

    async def get_by_email(self, user_email: str):
        result = await self.db_table.execute(select(UserTable).where(UserTable.email == user_email))
        return result.scalar_one_or_none()

    async def get_by_id(self, user_id: int):
        result = await self.db_table.execute(select(UserReduce).where(UserTable.id == user_id))
        return result.scalar_one_or_none()