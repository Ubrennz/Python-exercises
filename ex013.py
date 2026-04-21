salario_funcionario = float(input('Qual é o salário do funcionário? R$'))

salario_com_aumento = (0.15 * salario_funcionario + salario_funcionario)

print(f'Um funcionário q ganhava R${salario_funcionario}, com 15% de aumento, passa a receber R${salario_com_aumento:.2f}')
