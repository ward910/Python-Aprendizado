lista = []
pares = []
impares = []

while True:
	n = int(input('Digite um número: '))
	
	lista.append(n)
	continuar = ' '
	while continuar not in 'SN':
		continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	
	if continuar == 'N':
		break

for n in lista:
		if n % 2 == 0:
			pares.append(n)
		else:
			impares.append(n)

pares.sort()
impares.sort()
print('-=' * 30)
print(f'A lista completa {lista}')
print(f'A lista de pares {pares}')
print(f'A lista de impares {impares}')
