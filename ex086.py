matriz = []
linha = []

for i in range(0, 3):
    for j in range(0, 3):
        linha.append(int(input('Digite um número: ')))

    matriz.append(linha[:])
    linha.clear()

for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz)):
        if coluna == 0:
            print('|', matriz[linha][coluna], end=' | ')
        else:
            print(matriz[linha][coluna], end=' | ')
    print(end='\n')