km_viagem = int(input('Digite quantos km/h tem a viagem: '))

if km_viagem <= 200:
    print(f'O valor da viagem é de {0.50 * km_viagem}')
elif km_viagem > 200:
    print(f'O valor da viagem é de {0.45 * km_viagem}')
else:
    raise ValueError('Digite um valor válido')