numeros = []

numeros_digitados = 0

while True:
    num = int(input('Digite um número ou 0 para sair: '))

    if num == 0:
        break

    numeros.append(num)
    numeros_digitados += 1

numeros.sort(reverse=True)
print(numeros)

if 5 in numeros:
    print(f'O valor 5 foi digitado e está na lista na posição {numeros.index(5)}')
else:
    print('O valor 5 não foi digitado e não está na lista')