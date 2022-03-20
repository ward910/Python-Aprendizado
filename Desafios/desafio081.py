lista = []

while True:
	n = int(input('Digite um valor: '))
	
	lista.append(n)
	
	continuar = ' '
	while continuar not in 'SN':
		continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	
	if continuar == 'N':
		break

print('-=' * 30)

print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)

print(f'Os valores em ordem decrescente são {lista}')

if lista.count(5) != 0:
	print('O valor 5 faz parte da lista')
else:
	print('O valor 5 não foi encontrado na lista')
