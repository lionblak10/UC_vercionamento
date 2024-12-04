situacao = ""
alunos = []
quantidade_aluno = float(input("quantos alunos deseja cadastrar"))
cont = 0
while cont < quantidade_aluno:
    nome=input("Digite o nome do aluno:")
    print(nome)
    n1 = float(input("nota1: "))
    n2 = float(input("nota1: "))
    n3 = float(input("nota1: "))
    n4 = float(input("nota1: "))
    
    faltas=int(input("Digite o númesro de faltas do aluno:"))
    media=(n1+n2+n3+n4)/4
    print(media)

    if media >=8:
        situacao = print("Você está aprovado")
    elif media >=5:
        recuperacao=float(input("Nota de recuperação "))
        if recuperacao >=(10-media):
            situacao = "Aprovado na recuperação"
        else:
            situacao="Reprovado na recuperação"
    else:
        situacao = "Reprovado por mediá"
    alunos.append([nome,faltas,media,situacao])
    cont=+1
    
print(alunos)
print("nome: ", nome)
print("Notas:", n1,n2,n3,n4)
print("faltas: ", faltas)
print("media ", media)
print("situação ", situacao)
print(quantidade_aluno)