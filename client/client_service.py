from client.client_repository import ClientRepository
from client.client_table import Client

class ClientService:
    def __init__(self, repo: ClientRepository):
        self.repo = repo

    async def create_new_client(self, client: Client) -> Client:
        return await self.repo.create(client)
