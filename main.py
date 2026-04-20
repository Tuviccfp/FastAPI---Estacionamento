from fastapi import FastAPI
from contextlib import asynccontextmanager
from client.client_router import router_client

from user.user_router import router_user


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     create_db_and_tables()
#     yield

app = FastAPI()

app.include_router(router_client)
app.include_router(router_user)
