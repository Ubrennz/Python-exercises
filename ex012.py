preco_produto = float(input('Qual é o preço do produto? R$'))

preco_com_desconto = (0.05 * preco_produto - preco_produto) * -1.0

print(f'O produto q custava R${preco_produto}, na promoção com desconto de 5% vai custar R${preco_com_desconto:.2f}')