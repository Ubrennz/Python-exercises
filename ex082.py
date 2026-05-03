numeros = []
impares = []
pares = []

while True:
    num = int(input('Digite um número ou 0 para sair: '))

    if num == 0:
        break

    numeros.append(num)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Todos os números: {numeros}')
print(f'Os números ímpares: {impares}')
print(f'Os números pares: {pares}')