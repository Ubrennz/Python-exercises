numeros = []

parar_loop = False

while not parar_loop:
    num = int(input('Digite um número: '))

    if not num in numeros:
        numeros.append(num)
    else:
        parar_loop = True

numeros.sort()
print(numeros)