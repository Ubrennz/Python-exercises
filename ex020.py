from random import sample

aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')

print(f'O aluno sorteado foi {sample([aluno1, aluno2, aluno3, aluno4], k=4)}')
