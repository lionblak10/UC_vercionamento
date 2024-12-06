import time  # Importa o módulo time, usado para adicionar pausas no programa

# Inicializa as variáveis de controle
situacao = ""
nome = nota1 = nota2 = nota3 = nota4 = faltas = situacao = media = 0  # Variáveis que irão armazenar os dados dos alunos
alunos = []  # Lista que armazenará os dados de todos os alunos cadastrados

# Solicita a quantidade de alunos que deseja cadastrar
quantidade_aluno = float(input("Quantos alunos deseja cadastrar:"))

# Loop principal do programa
while True:
    # Exibe o menu para o usuário escolher uma opção
    escolha_menu = int(input("\nEscolha uma opção: \n1. Cadastrar\n2. Relatório\n3. Encerrar\nEscolha uma dessas opções:"))

    if escolha_menu == 1:  # Caso o usuário escolha a opção de cadastrar um aluno
        cont = 0  # Contador de alunos cadastrados
        while cont < quantidade_aluno:  # Repete até cadastrar a quantidade desejada de alunos
            nome = input("Digite o nome do aluno:")  # Solicita o nome do aluno
            print(nome)  # Exibe o nome digitado

            # Solicita as 4 notas do aluno
            n1 = float(input("Nota 1: "))
            n2 = float(input("Nota 2: "))
            n3 = float(input("Nota 3: "))
            n4 = float(input("Nota 4: "))

            # Solicita o número de faltas do aluno
            faltas = int(input("Digite o número de faltas do aluno:"))

            # Calcula a média das notas
            media = (n1 + n2 + n3 + n4) / 4
            print("Média:", media)  # Exibe a média calculada

            # Define a situação do aluno com base na média
            if media >= 8:
                situacao = "Aprovado"
            elif media >= 5:  # Caso a média seja entre 5 e 7
                # Solicita a nota de recuperação se o aluno estiver em recuperação
                recuperacao = float(input("Nota de recuperação: "))
                if recuperacao >= (10 - media):  # Verifica se a nota de recuperação foi suficiente
                    situacao = "Aprovado na recuperação"
                else:
                    situacao = "Reprovado na recuperação"
            else:  # Se a média for abaixo de 5, o aluno é reprovado
                situacao = "Reprovado por média"

            # Adiciona os dados do aluno na lista 'alunos'
            alunos.append([nome, faltas, media, situacao])

            cont += 1  # Incrementa o contador para garantir que o loop pare após cadastrar a quantidade definida

        # Exibe os dados do aluno após o cadastro
        print("\nRelatório do aluno cadastrado:")
        print("Nome:", nome)
        print("Notas:", n1, n2, n3, n4)
        print("Faltas:", faltas)
        print("Média:", media)
        print("Situação:", situacao)
        print("Quantidade de alunos a cadastrar:", quantidade_aluno)

    elif escolha_menu == 2:  # Caso o usuário escolha a opção de exibir o relatório
        print("Processando...")
        time.sleep(4)  # Pausa de 4 segundos para simular o processamento

        # Exibe o relatório de todos os alunos cadastrados
        for i in alunos:
            print("-" * 50)
            print(f"\nNome: {i[0]}")
            print("Faltas:", i[1])  # Corrigido para mostrar as faltas (i[1] é o número de faltas)
            print("Média:", i[2])   # Corrigido para mostrar a média (i[2] é a média)
            print(f"Situação: {i[3]}\n")  # Situação do aluno
        print("-" * 50)

    elif escolha_menu == 3:  # Caso o usuário escolha a opção de encerrar
        print("Encerrando....")
        time.sleep(2)
        print("Você encerrou o Programa, Volte sempre!:)")
        break  # Sai do loop e encerra o programa

    else:  # Caso o usuário escolha uma opção inválida
        print("Opção inválida! Tente novamente.")
        time.sleep(1)