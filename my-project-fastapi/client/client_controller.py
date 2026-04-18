from typing import Annotated

from fastapi import Depends

from client.client_repository import ClientRepository
from client.client_service import ClientService
from client.client_table import Client


class ClientController:
    def __init__(self, service: ClientService):
        self.service = service

    def create_client_service(self, client: Client):
        return self.service.create_new_client(client)


def get_client_controller(db):
    repo = ClientRepository(db)
    service = ClientService(repo)
    return ClientController(service)

ClientControllerDep = Annotated[ClientController, Depends(get_client_controller)]