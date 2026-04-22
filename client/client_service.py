from client.client_repository import ClientRepository
from client.client_table import Client, ClientDTO


class ClientService:
    def __init__(self, repo: ClientRepository):
        self.repo = repo

    async def create_new_client(self, client: Client) -> Client:
        return await self.repo.create(client)

    async def get_all_clients(self):
        return await self.repo.get_all()

    async def get_client_by_placa(self, client_placa_carro: str):
        return await self.repo.get_by_placa(client_placa_carro)

    async def get_client_by_id(self, client_id: int):
        return await self.repo.get_by_id(client_id)

    async def delete_client_by_id(self, client_id: int):
        return await self.repo.delete_by_id(client_id)

    async def update_client(self, client_id: int, client_dto: ClientDTO):
        return await self.repo.update_client(client_id, client_dto)