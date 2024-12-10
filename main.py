    #CADASTRO DE USUÁRIO E SENHA
    #MENU PRINCIPAL
saldo = 0.0 #variavel 
while True:
    print("Bem vindo! \n1. Cadastrar\n2. login\n3. Encerrar\nEscolha uma dessas opções:")
    #LER A ESCOLHA DO USUÁRIO
    escolha_menu = int(input()) #Lê a escolha como um número

    # SE O USUÁRIO ESCOLHER CADASTRO
    if escolha_menu == 1:
        #Criar um usuário e uma senha com tipo string
        usuario = input("Crie um nome de usuário:")
        senha = input("Crie uma senha:")
    elif escolha_menu == 2: #se usuário escolher login
        #comparar as inf. cadastradas com uma leitura
        login_usuario = input("Digite seu usuário:")
        login_senha = input("Digite sua senha:")
        escolha_principal = int(input())
        if login_usuario == usuario and login_senha == senha:
            print("LOGIN REALIZADO COM SUCESSO")
            print("Bem vindo! ", usuario)
            
            while True:
                print("1. Deposito 2. sacar 3. Extrato 4. Encerrar")
                valor_deposito = int(input())
                saldo = saldo + valor_deposito #Atualizar o valor
                
        elif escolha_principal == 3: #saque
             valor_pix = float(input("Digite o valor do pix"))
             valor_saque = float(input("Digite o valor do saque"))
             senha_saque = input("Digite sua senha: ")

             if senha_saque == senha:
                saldo = saldo - valor_saque
             else:
                print("Senha incorreta")
        elif escolha_principal == 4:
            senha_extrato = input("Digite sua senha ")
            if senha_extrato == senha:

                print("Extrato ", saldo)
            else:
                print("senha incorreta")
        elif escolha_principal == 5:
            senha_encerrar = input("Digite sua senha")
            if senha_encerrar == senha:
                break
            else:
                print("senha")
        else:                                         #SE LOGIN CORRETO, ENTRA NO
            print("USUÁRIO OU SENHA INCORRETOS")      #MENU PRINCIPAL DO APP
        