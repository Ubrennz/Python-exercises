alunos = []
dados_alunos = []

while True:
    nome_aluno = input('Digite o nome do aluno ou digite 0 para parar: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    dados_alunos.append(nome_aluno)
    dados_alunos.append(nota1)
    dados_alunos.append(nota2)

    alunos.append(dados_alunos[:])
    dados_alunos.clear()

    opcao = int(input('Digite 0 para parar ou 1 para continuar: '))

    if opcao == 0:
        break
    elif opcao == 1:
        continue
    else:
        raise ValueError('Opção inválida')

for aluno in alunos:
    print(f'{aluno[0]} - {aluno[1] / aluno[2] if aluno[1] > aluno[2] else aluno[2] / aluno[1]} ')
