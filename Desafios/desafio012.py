produto = float(input('Qual é o preço do produto: R$'))
desconto = produto - (produto * (5 / 100))

print(f'O produto que custava R${produto}, na promoção com desconto de 5% vai custa R${desconto:.2f}')
