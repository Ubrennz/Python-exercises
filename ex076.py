produtos = ('Pão', 1, 'Manteiga', 5.70, 'Sabonete', 1.99, 'Sabão em pó', 6.00)

for i in range(0, len(produtos), 2):
    print(f'{produtos[i]}..................R${produtos[i + 1]}')