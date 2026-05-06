matriz = []
linha = []

for i in range(0, 3):
    for j in range(0, 3):
        linha.append(int(input('Digite um número: ')))

    matriz.append(linha[:])
    linha.clear()

soma_valores_pares = 0
soma_valores_terceira_coluna = 0
maior_valor_segunda_linha = 0

for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz)):
        if matriz[linha][coluna] % 2 == 0:
            soma_valores_pares += matriz[linha][coluna]

        if coluna == 2:
            soma_valores_terceira_coluna += matriz[linha][coluna]

        if linha == 1 and matriz[linha][coluna] > maior_valor_segunda_linha:
            maior_valor_segunda_linha = matriz[linha][coluna]

        print(f'[{matriz[linha][coluna]}]', end=' ')
    print(end='\n')

print(f'Soma dos valores pares: {soma_valores_pares}')
print(f'Soma dos valores da terceira coluna: {soma_valores_terceira_coluna}')
print(f'Maior valor da segunda linha: {maior_valor_segunda_linha}')
