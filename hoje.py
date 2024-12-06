import time 
nome=nota1=nota2=nota3=nota4=faltas=situacao=media=0 
alunos =[] 
nota1 = 0 
while True: 
    escolha_menu=int(input("\nEscolha uma opção: \n1.Cadastrar\n2.relatorio\n3.encerrar\nEscolha uma dessas opçoes: "))
    if escolha_menu ==1: escolha_usuario=int (input("Quantos alunos você deseja cadastrar? "))
    cont=0 
    while cont < escolha_usuario: nome =input("\nDigite o nome do aluno: ")

    nota1=float(input("Digite a nota do 1°bimestre: "))
    nota2=float(input("Digite a nota do 2°bimestre: ")) 
    nota3=float(input("Digite a nota do 3°bimestre: ")) 
    nota4=float(input("Digite a nota do 4°bimestre: ")) 

    faltas=int(input("Digite as faltas do aluno: ")) 
    media=(nota1+nota2+nota3+nota4)/4
    print (f"A media do aluno foi: {media}")