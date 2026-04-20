from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session, select
from client.client_table import Client

class ClientRepository:
    def __init__(self, db_table: AsyncSession):
        self.db_table = db_table

    async def create(self, client: Client) -> Client:
        self.db_table.add(client)
        await self.db_table.commit()
        await self.db_table.refresh(client)
        return client

    async def get_by_placa(self, client_placa_carro: str):
        result = await self.db_table.execute(select(Client).where(
            client_placa_carro == Client.placa_carro
        ))
        return result.first()