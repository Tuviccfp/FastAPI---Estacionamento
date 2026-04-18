from controller.controller import controllerFunction
def mainProgram():
    while True:
        print("Menu: \n 1 - Cadastrar cliente \n 2 - Listar clientes \n 3 - Buscar cliente por ID \n 4 - Atualizar cliente \n 5 - Deletar cliente \n Digite 'sair' para encerrar o programa.")
        
        value = input("\n\nDigite o número da opção: ")
        if value.lower() == 'sair':
            print("Encerrando o programa. Até mais!")
            break
        controllerFunction(value)


if __name__ == '__main__':
    mainProgram()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
