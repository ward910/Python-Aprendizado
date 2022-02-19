listanum = ['N']

while True:
	num = int(input('Digite um valor: '))
	
	if listanum.count(num) == 0:
		listanum.append(num)
	else:
		print('Valor duplicado! Não vou adicionar...')
	
	continuar = ' '
	while continuar not in 'SN':
		continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	
	if continuar == 'N':
		break

print('Você digitou valores', sorted(listanum[1:]))
