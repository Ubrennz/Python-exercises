from random import randint
from time import sleep

numeros_sorteados = {}

for i in range(1, 5):
    numeros_sorteados[f'Jogador{i}'] = randint(1, 6)

dados_organizados = dict(sorted(numeros_sorteados.items(), key=lambda item: item[1]))

maior_numero = 0

for k, v in dados_organizados.items():
    if v > maior_numero:
        maior_numero = v

    print(f'O {k} tirou o número {v}')
    sleep(0.8)

for k, v in dados_organizados.items():
    if v == maior_numero:
        print(f'O vencedor é {k}, ele tirou o número {v}')
