import copy as copia

def cadastrar_funcionario(id, cont):
    # Função para cadastrar um funcionário. A função recebe o ID base e um contador,
    # que é utilizado para incrementar o ID do funcionário.

    print()
    print('-' * 20, 'MENU CADASTRAR FUNCIONÁRIO', '-' * 20)

    id += cont  # Incrementa o ID com base no contador para gerar um novo ID único para o funcionário.

    print(f'ID do Funcionário: {id}')

    while True:
        nome = input('Por favor, entre com o nome do Funcionário: ').lower()

        # Verifica se o nome é válido, permitindo apenas letras e espaços.
        if nome.replace(' ', '').isalpha():
            break
        else:
            print()
            print('Nome inválido. Entre com um nome válido (apenas letras e espaços).')

    while True:
        setor = input('Por favor, entre com o setor do Funcionário: ').lower()

        # Verifica se o setor é válido, permitindo apenas letras e espaços.
        if setor.replace(' ', '').isalpha():
            break
        else:
            print()
            print('Setor inválido. Entre com um setor válido (apenas letras e espaços).')

    while True:
        try:
            # Tenta converter o valor de salário em um número decimal.
            salario = float(input('Por favor, entre com o salário do Funcionário: '))
            break
        except ValueError:
            print()
            print('Salário inválido. Entre com um salário válido (apenas números).')

    # Cria um dicionário com as informações do funcionário.
    funcionario = {
        'ID': id,
        'NOME': nome,
        'SETOR': setor,
        'SALÁRIO': salario
    }

    # Adiciona o dicionário do funcionário à lista de funcionários usando uma cópia.
    lista_funcionarios.append(copia.copy(funcionario))

    print()
    print('Funcionário cadastrado com sucesso!')
    print()

def consultar_funcionarios():
    # Função para consultar funcionários cadastrados no sistema.

    while True:
        print()
        print('-' * 20, 'MENU CONSULTAR FUNCIONÁRIO', '-' * 20)
        print('1 - Consultar Todos os Funcionários')
        print('2 - Consultar Funcionário por id')
        print('3 - Consultar Funcionário(s) por setor')
        print('4 - Retornar')
        try:
            res = int(input('>>'))  # Captura a opção escolhida pelo usuário.

        except ValueError:
            print()
            print('Opção inválida. Por favor, tente novamente.')
            continue

        if res == 1:
            # Consulta todos os funcionários cadastrados.
            if len(lista_funcionarios) > 0:
                print('-' * 20)
                print()

                for funcionario in lista_funcionarios:
                    for chave, valor in funcionario.items():
                        print(chave, ':', valor)
                    print()

                print('-' * 20)

            else:
                print()
                print('+', '-' * 40, '+')
                print('| Ainda não há funcionários cadastrados... | ')
                print('+', '-' * 40, '+')

        elif res == 2:
            # Consulta um funcionário específico pelo ID.
            if len(lista_funcionarios) > 0:
                controlador = True

                while controlador:
                    try:
                        id_funcionario = int(input('Digite o id do funcionário: '))

                        funcionario_encontrado = False

                        for funcionario in lista_funcionarios:
                            if funcionario['ID'] == id_funcionario:
                                print('-' * 20)
                                print()

                                for chave, valor in funcionario.items():
                                    print(chave, ':', valor)

                                print()
                                print('-' * 20)
                                funcionario_encontrado = True
                                controlador = False
                                break

                        if not funcionario_encontrado:
                            print()
                            print('+', '-' * 34, '+')
                            print('| Não há funcionários com esse id... | ')
                            print('+', '-' * 34, '+')
                            break

                    except ValueError:
                        print()
                        print('Id inválido. Entre com um id válido (apenas números).')

            else:
                print()
                print('+', '-' * 40, '+')
                print('| Ainda não há funcionários cadastrados... | ')
                print('+', '-' * 40, '+')

        elif res == 3:
            # Consulta funcionários por setor.
            if len(lista_funcionarios) > 0:
                controlador = True

                while controlador:
                    setor_funcionario = input('Digite o setor do funcionário: ').lower()

                    # Verifica se o setor é válido.
                    if setor_funcionario.replace(' ', '').isalpha():
                        print('-' * 20)
                        print()

                        funcionario_encontrado = False

                        for funcionario in lista_funcionarios:
                            if funcionario['SETOR'] == setor_funcionario:

                                for chave, valor in funcionario.items():
                                    print(chave, ':', valor)

                                print()
                                funcionario_encontrado = True
                                controlador = False

                        if not funcionario_encontrado:
                            print('+', '-' * 42, '+')
                            print('| Não há funcionários atuando nesse setor... | ')
                            print('+', '-' * 42, '+')
                            print()

                        print('-' * 20)
                        break

                    else:
                        print()
                        print('Setor inválido. Entre com um setor válido (apenas letras e espaços).')

            else:
                print()
                print('+', '-' * 40, '+')
                print('| Ainda não há funcionários cadastrados... | ')
                print('+', '-' * 40, '+')

        elif res == 4:
            # Retorna ao menu principal.
            print()
            verdadeiro = True
            return verdadeiro

        else:
            print()
            print('Opção inválida. Por favor, tente novamente.')
            continue

def remover_funcionario():
    # Função para remover um funcionário do sistema.

    if len(lista_funcionarios) > 0:
        print()
        print('-' * 20, 'MENU REMOVER FUNCIONÁRIO', '-' * 20)

        controlador = True

        while controlador:
            try:
                id_funcionario = int(input('Digite o id do funcionário a ser removido: '))

                funcionario_encontrado = False

                for funcionario in lista_funcionarios:
                    if funcionario['ID'] == id_funcionario:
                        lista_funcionarios.remove(funcionario)  # Remove o funcionário da lista.
                        print()
                        print('Funcionário removido com sucesso!')
                        print()
                        print('-' * 56)
                        funcionario_encontrado = True
                        controlador = False
                        break

                if not funcionario_encontrado:
                    print()
                    print('+', '-' * 34, '+')
                    print('| Não há funcionários com esse ID... |')
                    print('+', '-' * 34, '+')
                    print()
                    break

            except ValueError:
                print()
                print('Id inválido. Por favor, digite um número válido.')

    else:
        print()
        print('+', '-' * 40, '+')
        print('| Ainda não há funcionários cadastrados... | ')
        print('+', '-' * 40, '+')
        print()

# Programa principal
lista_funcionarios = []  # Inicializa a lista que armazenará os funcionários.

id_global = 4934907  # ID base utilizado para gerar IDs únicos para os funcionários.

cont = 0  # Contador utilizado para incrementar o ID global.

print('Bem vindo(a) a empresa do Ederson Ramos')
print('-' * 56)

while True:
    print('-' * 20, 'MENU PRINCIPAL', '-' * 20)
    print('1 - Cadastrar Funcionários')
    print('2 - Consultar Funcionário(s)')
    print('3 - Remover Funcionário')
    print('4 - Sair')

    try:
        res = int(input('>>'))  # Captura a opção escolhida pelo usuário no menu principal.

        if res >= 1 and res <= 4:
            print('-' * 56)

            if res == 1:
                cont += 1  # Incrementa o contador de IDs para cada novo funcionário cadastrado.
                cadastrar_funcionario(id_global, cont)

            elif res == 2:
                while True:
                    quebrar = consultar_funcionarios()  # Chama a função de consulta de funcionários.

                    if quebrar == True:
                        break

            elif res == 3:
                remover_funcionario()  # Chama a função de remoção de funcionário.

            elif res == 4:
                print('Programa encerrado...')
                break

        elif res < 1 or res > 4:
            print()
            print('Opção inválida. Por favor, tente novamente. \n')

    except ValueError:
        print()
        print('Opção inválida. Por favor, tente novamente. \n')