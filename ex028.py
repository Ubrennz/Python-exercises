velocidade = int(input('Digite a velocidade q o carro está: '))

if velocidade > 80:
    print(f'Vc foi multado, vc está a {velocidade}km/h e o valor da multa é de {(velocidade - 80) * 7}')
else:
    print(f'Vc não foi multado, a sua velocidade está abaixo de 80Km/h')