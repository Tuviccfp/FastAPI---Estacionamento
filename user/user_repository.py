
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session, select, update

from user.user_table import UserTable, UserReduce, UserDTOUpdate


class UserRepository:
    def __init__(self, db_table: AsyncSession):
        self.db_table = db_table

    async def create(self, user: UserTable):
        self.db_table.add(user)
        await self.db_table.commit()
        await self.db_table.refresh(user)
        return UserReduce(id=user.id, email=user.email, nome=user.nome, role=user.role)

    async def get_all(self, offset: int = 10, limit: int = 10):
        result = await self.db_table.execute(select(UserTable))
        return result.scalars().all()

    async def get_by_email(self, user_email: str):
        result = await self.db_table.execute(select(UserTable).where(UserTable.email == user_email))
        return result.scalar_one_or_none()

    async def get_by_id(self, user_id: int | None):
        result = await self.db_table.execute(select(UserTable).where(UserTable.id == user_id))
        return result.scalar_one_or_none()

    async def delete_by_id(self, user_id: int):
        user = await self.get_by_id(user_id)
        if not user:
            return False
        await self.db_table.delete(user)
        await self.db_table.commit()
        return True

    async def update_user(self, user_id: int, user: UserTable):
        await self.db_table.execute(
            update(UserTable)
                .where(UserTable.id == user_id)
                .values(nome=user.nome, email=user.email, password=user.password))
        await self.db_table.commit()
        result = await self.db_table.execute(select(UserTable).where(UserTable.id == user_id))
        return result.scalar_one_or_none()