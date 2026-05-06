from random import randint

mega_sena = []
jogos = []

qtde_jogos = int(input('Digite quantos jogos serão gerados: '))

for i in range(0, qtde_jogos):
    for c in range(0, 6):
        jogos.append(randint(1, 60))

    jogos.sort()
    mega_sena.append(jogos[:])
    jogos.clear()

for p, jogo in enumerate(mega_sena):
    print(f'Jogo {p}: {jogo}')
