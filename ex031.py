from datetime import date

ano = int(input('Digite um ano para saber se ele é bissexto ou digite 0 para saber o ano atual: '))
ano_bissxto = date.today().year / 4 if ano == 0 else ano / 4

if ano_bissxto.is_integer():
    print(f'O ano de {ano} é bissexto!!')
else:
    print(f'O ano de {date.today().year if ano == 0 else ano} não é bissexto.')

