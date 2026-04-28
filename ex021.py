nome = input('Digite o seu nome completo: ')

print(f'Nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Nome com todas as letras minúculas: {nome.lower()}')
print(f'Total de letras sem considerar espaços: {len(nome.replace(' ', ''))}')
print(f'Número de letras do primeiro nome: {len(nome.split()[0])}')