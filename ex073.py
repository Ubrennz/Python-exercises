times = ('Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo', 'Athletico-PR', 'Bahia',
         'Coritiba', 'Botafogo', 'Bragantino', 'Vasco', 'Grêmio', 'Cruzeiro', 'Vitória',
         'Corinthians', 'Atlético-MG', 'Internacional', 'Santos', 'Mirassol', 'Remo', 'Chapecoense')

print(f'Os 5 primeiros colocados: {times[0:6]}')
print(f'Os 4 últimos colocados: {times[16:]}')

tupla_ordenada = tuple(sorted(times))

print(f'Lista de times ordenada: {tupla_ordenada}')
print(f'Posição da Chapecoense: {times.index('Chapecoense') + 1}')