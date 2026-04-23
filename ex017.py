from math import hypot

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

print(f'A hipotenusa do triângulo é de {hypot(cateto_oposto, cateto_adjacente)}')