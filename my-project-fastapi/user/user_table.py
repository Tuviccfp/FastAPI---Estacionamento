from sqlmodel import SQLModel, Field


class UserTable(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(index=True, nullable=False)
    email: str = Field(index=True, nullable=False)
    password: str = Field(nullable=False)
