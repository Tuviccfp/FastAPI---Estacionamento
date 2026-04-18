import sqlite3
import os
from .models import cliente

db_path = os.path.join(os.path.dirname(__file__), "database.sqlite")


def connect_db():
    conn = sqlite3.connect(db_path)
    cliente.create_cliente_table(conn)
    # Cria a tabela cliente se ela não existir
    return conn
