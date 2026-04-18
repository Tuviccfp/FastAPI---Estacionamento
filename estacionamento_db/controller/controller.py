from database.connection import connect_db
from repository.cliente_repository import ClienteRepository
from service.cliente_service import ClienteService

def controllerFunction(input_value):
    conn = connect_db()

    clienteRepo = ClienteRepository(conn)
    clienteService = ClienteService(clienteRepo)

    match input_value:
        case "1":
            print("Cadastrar cliente \n")
            name = input("Digite o nome do cliente: \n")
            email = input("Digite o email do cliente: \n")
            placa_carro = input("Digite a placa do carro do cliente: \n")
            cliente = {"nome": name, "email": email, "placa_carro": placa_carro}
            clienteService.criar_cliente(cliente)
            print("Cliente cadastrado com sucesso!")
        case "2":
            print("Listar clientes")
            clientes = clienteService.listar_clientes_todos()
            for cliente in clientes:
                print(f"\nID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}, Placa do Carro: {cliente[3]}")   
        case "3":
            print("Buscar cliente por ID")
            client_id = input("Digite o ID do cliente: ")
            cliente = clienteService.obter_cliente_por_id(client_id)
            if cliente:
                print(f"\nID: {cliente['id']}, Nome: {cliente['nome']}, Email: {cliente['email']}, Placa do Carro: {cliente['placa_carro']}")
            else:
                print("Cliente não encontrado.")
        case "4":
            print("Atualizar cliente")
            client_id = input("Digite o ID do cliente a ser atualizado: ")
            nome = input("Digite o novo nome do cliente (deixe em branco para não alterar): ")
            email = input("Digite o novo email do cliente (deixe em branco para não alterar): ")
            placa_carro = input("Digite a nova placa do carro do cliente (deixe em branco para não alterar): ")
            cliente = { "nome": nome, "email": email, "placa_carro": placa_carro }
            clienteService.atualizar_cliente(client_id, cliente)
            print("Cliente atualizado com sucesso!")
        case "5":
            print("Deletar cliente")
            client_id = input("Digite o ID do cliente a ser deletado: ")
            clienteService.deletar_cliente(client_id)
            print("Cliente deletado com sucesso!")
        case _:
            print("Opção inválida. Por favor, tente novamente.")
    conn.close()