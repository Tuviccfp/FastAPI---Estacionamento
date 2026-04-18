class ClienteService:
    def __init__(self, cliente_repository):
        self.cliente_repository = cliente_repository

    def criar_cliente(self, cliente):
        # Lógica para criar um cliente
        return self.cliente_repository.save_client(cliente)

    def listar_clientes_todos(self):
        # Lógica para listar todos os clientes
        return self.cliente_repository.get_all_clients()

    def obter_cliente_por_id(self, cliente_id):
        # Lógica para obter um cliente pelo ID
        return self.cliente_repository.get_client_by_id(cliente_id)

    def atualizar_cliente(self, cliente_id, nome=None, email=None, placa_carro=None):
        # Lógica para atualizar um cliente
        cliente = self.cliente_repository.get_client_by_id(cliente_id)
        if not cliente:
            return None
        
        if nome:
            cliente["nome"] = nome
        if email:
            cliente["email"] = email
        if placa_carro:
            cliente["placa_carro"] = placa_carro

        return self.cliente_repository.update_client(cliente_id, cliente)

    def deletar_cliente(self, cliente_id):
        # Lógica para deletar um cliente
        return self.cliente_repository.delete_client(cliente_id)