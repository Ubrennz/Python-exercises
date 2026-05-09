def linhas():
    print(20 * '-=-')

jogador = {}

jogador['Nome'] = input('Nome do jogador: ')

num_partidas = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))

gols_jogador = []
total_de_gols = 0

for i in range(1, num_partidas + 1):
    numero_de_gols = int(input(f'Quantos gols na partida {i}? '))
    gols_jogador.append(numero_de_gols)
    total_de_gols += numero_de_gols

jogador['Gols'] = gols_jogador
jogador['Total'] = total_de_gols

linhas()
print(jogador)
linhas()

for k, v in jogador.items():
    print(f'{k} - {v}')

linhas()
print(f'O jogador {jogador['Nome']} jogou {len(gols_jogador)} partidas.')
for i in range(0, len(gols_jogador)):
    print(f'-> Na partida {i + 1}, fez {gols_jogador[i]} gols')

print(f'Foi um total de {jogador['Total']} gols')
