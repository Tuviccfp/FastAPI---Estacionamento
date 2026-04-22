from fastapi import APIRouter

from client.client_table import Client, ClientDTO
from client.client_controller import ClientControllerDep
from middleware.auth.auth import CurrentUser

router_client = APIRouter()

@router_client.get("/ola")
async def root():
    return {"message": "Hello World"}

@router_client.post("/new-client")
async def new_client(client: Client, controller: ClientControllerDep, current_user: CurrentUser):
    created_client = await controller.create_client_service(client)
    return created_client

@router_client.get("/get-all-clients")
async def get_all_clients(controller: ClientControllerDep, current_user: CurrentUser):
    return await controller.get_all_clients()

@router_client.get("/get-client-by-placa/{client_placa_carro}")
async def get_client_by_placa(client_placa_carro: str, controller: ClientControllerDep, current_user: CurrentUser):
    return await controller.get_client_by_placa(client_placa_carro)

@router_client.get("/get-client-by-id/{client_id}")
async def get_client_by_id(client_id: int, controller: ClientControllerDep, current_user: CurrentUser):
    return await controller.get_client_by_id(client_id)

@router_client.delete("/delete-client-by-id/{client_id}")
async def delete_client_by_id(client_id: int, controller: ClientControllerDep, current_user: CurrentUser):
    return await controller.delete_client_by_id(client_id)

@router_client.put("/update-client/{client_id}")
async def update_client(client_id: int, client: ClientDTO, controller: ClientControllerDep, current_user: CurrentUser):
    return await controller.update_client(client_id, client)
