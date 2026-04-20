from pydantic.v1.dataclasses import dataclass
from sqlmodel import SQLModel, Field


@dataclass
class UserEmailDTO(SQLModel):
    email: str

@dataclass
class UserReduce(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(index=True, nullable=False)
    email: str = Field(index=True, nullable=False)
    role: str = Field(default="basic", nullable=False, index=True)

class UserTable(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(index=True, nullable=False)
    email: str = Field(index=True, nullable=False)
    role: str = Field(index=True, nullable=False)
    password: str = Field(nullable=False)
