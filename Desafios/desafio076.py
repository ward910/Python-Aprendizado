print('-'*40)
print('Listagem de Preços'.upper())
print('-'*40)

produtos = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Cardeno', 15.80,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livros', 34.90)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')





