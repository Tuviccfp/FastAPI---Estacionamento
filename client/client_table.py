from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class Client(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(index=True, nullable=False)
    email: str = Field(index=True, nullable=False)
    placa_carro: str = Field(index=True, nullable=False)

class ClientDTO(BaseModel):
    nome: str
    email: str
    placa_carro: str
    