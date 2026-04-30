a = float(input('Digite o lado A do triângulo: '))
b = float(input('Digite o lado B do triângulo: '))
c = float(input('Digite o lado C do triângulo: '))

if a + b > c and a + c > b and b + c > a:
    print(f'Os lados: {a}, {b}, {c} pode formar um triângulo')
else:
    print(f'Os lados: {a}, {b}, {c} NÃO pode formar um triângulo')