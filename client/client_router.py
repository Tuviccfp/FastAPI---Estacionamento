from fastapi import APIRouter, Depends, HTTPException
from httpx import HTTPError
from pip._internal.cli import status_codes

from database.sql_connect import SessionDep
from client.client_repository import ClientRepository
from client.client_service import ClientService
from client.client_table import Client
from database.sql_connect import get_session
from client.client_controller import ClientControllerDep

router_client = APIRouter()

@router_client.get("/ola")
async def root():
    return {"message": "Hello World"}

@router_client.post("/new-client")
def new_user(client: Client, controller: ClientControllerDep) -> Client:
    created_client = controller.create_client_service(client)
    return created_client