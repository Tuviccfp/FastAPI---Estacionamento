from fastapi.params import Depends
from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

sqlite_file_name = "database.db"
sqlite_url = f"sqlite+aiosqlite:///{sqlite_file_name}"

engine = create_async_engine(sqlite_url)

async_factory = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with async_factory() as async_session:
        yield async_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]
