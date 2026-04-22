from pydantic import BaseModel
from pydantic.v1.dataclasses import dataclass
from sqlmodel import SQLModel, Field


@dataclass
class UserEmailDTO(SQLModel):
    email: str

class UserReduce(BaseModel):
    id: int
    nome: str
    email: str
    role: str

class UserDTOUpdate(BaseModel):
    nome: str
    email: str
    password: str

class UserTable(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(index=True, nullable=False)
    email: str = Field(index=True, nullable=False)
    role: str = Field(index=True, nullable=False)
    password: str = Field(nullable=False)
