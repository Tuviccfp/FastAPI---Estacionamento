def create_cliente_table(conn):
    client_cursor = conn.cursor()

    client_cursor.execute(
        "CREATE TABLE IF NOT EXISTS cliente ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "nome VARCHAR(100), "
        "email VARCHAR(100), "
        "placa_carro VARCHAR(20))"
    )
    conn.commit()
