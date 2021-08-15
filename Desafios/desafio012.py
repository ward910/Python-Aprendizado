produto = float(input('Qual é o preço do produto: '))
desconto = produto - (produto * (5 / 100))

print(f'O produto que custava R${produto}, na promoção com desconto de 5% vai valer R${desconto:.2f}')
