frase = input('Digite um frase qualquer: ')

print(f'A letra A aparece {frase.upper().count('A')}')
print(f'A letra A aparece na primeira vez na posição {frase.upper().find('A')}')
print(f'A letra A aparece última pela vez na posição {frase.upper().rfind('A')}')
