diasAlugados = int(input('Quantos dias alugados? '))
diasRodados = float(input('Quantos Km rodados? '))

dias = diasAlugados * 60 
km = diasRodados * 0.15

pago = dias + km
print(f'Preço R${pago:.2f}')