from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session, select
from client.client_table import Client, ClientDTO


class ClientRepository:
    def __init__(self, db_table: AsyncSession):
        self.db_table = db_table

    async def create(self, client: Client):
        self.db_table.add(client)
        await self.db_table.commit()
        await self.db_table.refresh(client)
        return client

    async def get_all(self):
        result = await self.db_table.execute(select(Client))
        return result.scalars().all()

    async def get_by_placa(self, client_placa_carro: str):
        result = await self.db_table.execute(select(Client).where(
            client_placa_carro == Client.placa_carro
        ))
        return result.first()

    async def get_by_id(self, client_id: int):
        result = await self.db_table.execute(select(Client).where(
            client_id == Client.id
        ))
        return result.first()

    async def delete_by_id(self, client_id: int):
        await self.db_table.delete(client_id)
        await self.db_table.commit()

    async def update_client(self, client_id: int, client_dto: ClientDTO):
        await self.db_table.execute(
            update(Client)
                .where(Client.id == client_id)
                .values(nome=client_dto.nome, email=client_dto.email, placa_carro=client_dto.placa_carro))
        await self.db_table.commit()
        result = await self.db_table.execute(select(Client).where(Client.id == client_id))
        return result.scalar_one_or_none()