pessoas = []
dados_pessoas = []

pessoas_cadastradas = 0

while True:
    nome = input('Digite o nome da pessoa ou digite 0 para sair: ')

    if nome == '0':
        break

    peso = float(input('Digite o peso da pessoa: '))

    dados_pessoas.append(nome)
    dados_pessoas.append(peso)
    pessoas.append(dados_pessoas[:])
    pessoas_cadastradas += 1
    dados_pessoas.clear()

maior_peso = 0.0
menor_peso = 0.0

for pessoa in pessoas:
    if pessoa[1] >= pessoas[0][1]:
        maior_peso = pessoa[1]

    if pessoa[1] <= pessoas[0][1]:
        menor_peso = pessoa[1]


print(maior_peso)
print(menor_peso)