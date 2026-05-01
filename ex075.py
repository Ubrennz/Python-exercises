n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))

numeros = (n1, n2, n3, n4)

print(f'O valor 9 apareceu {numeros.count(9)}')
print(f'Primira posiçào q o valor 3 aparece: {numeros.index(3)}')

print('Os valores pares foram: ', end='')
for numero in numeros:
    if numero % 2 == 0:
        print(numero , end=' ')
