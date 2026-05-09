alunos = {}

alunos['Nome'] = input('Nome do aluno: ')
alunos['Média'] = float(input('Digite a média do aluno: '))
alunos['Situação'] = 'reprovado' if alunos['Média'] < 7.0 else 'Aprovado'

for k, v in alunos.items():
    print(f'{k} é {v}')

print(max(alunos['Média']))