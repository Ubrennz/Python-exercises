numeros = []

for i in range(0, 5):
    numeros.append(int(input('Digite um número: ')))

maior = max(numeros)
menor = min(numeros)

print(f'O maio número é {maior}, e sua posição é {numeros.index(maior)}')
print(f'O menor número é {menor}, e sua posição é {numeros.index(menor)}')
