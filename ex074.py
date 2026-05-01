from random import randint

numeros_aleatorios = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))

print(f'Números gerados: {numeros_aleatorios}')

tupla_ordenada = tuple(sorted(numeros_aleatorios))

print(f'Menor número dentro da tupla: {tupla_ordenada[0]}')
print(f'Maior número dentro da tupla: {tupla_ordenada[-1]}')