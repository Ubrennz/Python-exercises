from datetime import date

dados_trabalhador = {}

dados_trabalhador['Nome'] = input('Nome: ')
dados_trabalhador['Idade'] = date.today().year - int(input('Ano de nascimento: '))
dados_trabalhador['Carteira de trabalho'] = input('Carteira de trabalho ou (0 não tem): ')

if dados_trabalhador['Carteira de trabalho'] != '0':
    dados_trabalhador['Ano de contratação'] = int(input('Ano de contratação: '))
    dados_trabalhador['Salário'] = float(input('Salário R$'))

print(dados_trabalhador)

for k, v in dados_trabalhador.items():
    print(f'{k} é {v}')

if dados_trabalhador['Carteira de trabalho'] != '0':
    aposentadoria = dados_trabalhador['Ano de contratação'] - date.today().year + dados_trabalhador['Idade'] + 35
    print(f'O trabalhador vai se aposentar com {aposentadoria:.2f} anos')
