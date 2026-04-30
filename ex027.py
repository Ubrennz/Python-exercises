from random import randint

num = int(input('Digite um valor entre 0 e 5: '))

if num < 0 or num > 5:
    raise ValueError('Digite um valor entre 0 e 5')

rand = randint(0, 5)
if num == rand:
    print(f'Parabéns, vc acertou!! A maquina pensou {rand}')
else:
    print(f'Vc errou! A maquina pensou {rand}')
