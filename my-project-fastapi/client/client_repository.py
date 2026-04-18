from sqlmodel import Session, select
from client.client_table import Client

class ClientRepository:
    def __init__(self, db_table: Session):
        self.db_table = db_table

    def create(self, client: Client) -> Client:
        self.db_table.add(client)
        self.db_table.commit()
        self.db_table.refresh(client)
        return client

    def get_by_placa(self, client_placa_carro: str):
        result = self.db_table.exec(select(Client).where(
            client_placa_carro == Client.placa_carro
        ))
        return result.first()