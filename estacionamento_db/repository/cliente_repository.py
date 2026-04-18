
class ClienteRepository:
    def __init__(self, connection):
        self.connection = connection

    def save_client(self, cliente):
        try:
            client_cursor = self.connection.cursor()
            client_cursor.execute(
                "INSERT INTO cliente (nome, email, placa_carro) VALUES (?, ?, ?)",
                (cliente["nome"], cliente["email"], cliente["placa_carro"])
            )
            self.connection.commit()
        except Exception as e:
                print(f"Erro ao salvar cliente: {e}")
                self.connection.rollback()


    def get_all_clients(self):
        try:
            client_cursor = self.connection.cursor()
            client_cursor.execute("SELECT * FROM cliente")
            return client_cursor.fetchall()
        except Exception as e:
            print(f"Erro ao listar clientes: {e}")
            
    def get_client_by_id(self, client_id):
        try:
            client_cursor = self.connection.cursor()
            client_cursor.execute("SELECT * FROM cliente WHERE id = ?", (client_id,))
            row = client_cursor.fetchone()
            return {"id": row[0], "nome": row[1], "email": row[2], "placa_carro": row[3]} if row else None
        except Exception as e:
            print(f"Erro ao buscar cliente: {e}")
            return None

    def update_client(self, client_id, cliente):
        try:
            client_cursor = self.connection.cursor()
            client_cursor.execute(
                "UPDATE cliente SET nome = ?, email = ?, placa_carro = ? WHERE id = ?",
                (cliente["nome"], cliente["email"], cliente["placa_carro"], client_id)
            )
            self.connection.commit()
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")
            self.connection.rollback()

    def delete_client(self, client_id):
        try:
            client_cursor = self.connection.cursor()
            client_cursor.execute("DELETE FROM cliente WHERE id = ?", (client_id,))
            self.connection.commit()
        except Exception as e:
            print(f"Erro ao excluir cliente: {e}")
            self.connection.rollback()
