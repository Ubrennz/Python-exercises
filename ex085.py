numeros = []
impares = []
pares = []

for i in range(0, 7):
    numeros.append(int(input('Digite um número: ')))

numeros.sort()

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Os valores ímpares: {impares}')
print(f'Os valores pares: {pares}')
