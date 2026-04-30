salario = float(input('Qual é o salário do funcionário? R$'))
salario_com_aumento = 0.15 * salario + salario if salario <= 1250 else 0.10 * salario + salario

print(f'O salário com aumento é {salario_com_aumento}')
