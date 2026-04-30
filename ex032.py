lista = []

for i in range(0, 3):
    lista.append(int(input('Digite um valor: ')))

lista.sort()
print(f'O maior número é {lista[-1]}')
print(f'O maior número é {lista[0]}')
