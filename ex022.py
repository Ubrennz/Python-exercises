num = int(input('Digite um número entre 0 e 9999: '))

if num < 0 or num > 9999:
    raise ValueError('Digite um valor entre 0 e 9999')

num_str = str(num)

tamanho = len(num_str)
if tamanho >= 1:
    print(f'Unidade: {num_str[-1]}')

if tamanho >= 2:
    print(f'Dezena: {num_str[-2]}')

if tamanho >= 3:
    print(f'Centena: {num_str[-3]}')

if tamanho >= 4:
    print(f'Milhar: {num_str[-4]}')