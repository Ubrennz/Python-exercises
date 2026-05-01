numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

num_digitado = int(input('Digite um número entre 0 e 20: '))

if num_digitado < 0 or num_digitado > 20:
    raise ValueError('Digite entre 0 e 20')

print(numeros[num_digitado])