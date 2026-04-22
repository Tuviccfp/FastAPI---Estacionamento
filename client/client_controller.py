from typing import Annotated

from fastapi import Depends

from database.sql_connect import SessionDep
from client.client_repository import ClientRepository
from client.client_service import ClientService
from client.client_table import Client, ClientDTO


class ClientController:
    def __init__(self, service: ClientService):
        self.service = service

    async def create_client_service(self, client: Client):
        return await self.service.create_new_client(client)

    async def get_all_clients(self) -> list[Client]:
        return await self.service.get_all_clients()

    async def get_client_by_placa(self, client_placa_carro: str) -> Client:
        return await self.service.get_client_by_placa(client_placa_carro)

    async def get_client_by_id(self, client_id: int) -> Client:
        return await self.service.get_client_by_id(client_id)

    async def delete_client_by_id(self, client_id: int):
        return await self.service.delete_client_by_id(client_id)

    async def update_client(self, client_id: int, client_dto: ClientDTO) -> Client:
        return await self.service.update_client(client_id, client_dto)

def get_client_controller(db: SessionDep):
    repo = ClientRepository(db)
    service = ClientService(repo)
    return ClientController(service)

ClientControllerDep = Annotated[ClientController, Depends(get_client_controller)]