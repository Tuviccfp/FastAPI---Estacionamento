from fastapi import FastAPI
from contextlib import asynccontextmanager
from client.client_router import router_client
from database.sql_connect import create_db_and_tables

from user.user_router import router_user


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router_client)
app.include_router(router_user)

