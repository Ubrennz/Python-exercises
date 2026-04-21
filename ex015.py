# dia R$60, km R$0,15
dias_alugados = int(input('Digite quantos dias o carro foi alugado: '))
km_rodados = int(input('Digite quantos KMs o carro rodou: '))

valor_a_ser_pago = (dias_alugados * 60) + (km_rodados * 0.15)

print(f'O total a pagar é de R${valor_a_ser_pago:.2f}')
