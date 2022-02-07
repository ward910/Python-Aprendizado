ListaCompras = {}; soma = cont = menorValor = 0
nome = ''

while True:
	produto = str(input('Nome do Produtor: ')).strip()
	preco = int(input('Preço: R$')); menorValor += preco

	ListaCompras[produto] = preco 

	continuar = ' '
	while continuar not in 'SN':
		continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

	if continuar == 'N':
		break

for key, value in ListaCompras.items():
	soma += int(value)

	if value > 1000:
		cont += 1

	if value < menorValor:
		nome = key
		menorValor = value
print('{:-^40}'.format('FIM DO PROGRAMA'))

print(f'O total da compra foi R${float(soma):.2f}')
print(f'Temos {cont} produtos custando mais de R$1000')
print(f'O produto mais barato foi {nome} que custa {float(menorValor):.2f}')
