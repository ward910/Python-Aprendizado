pessoas = []
maior = 0
menor = pow(60, 2)

while True:
	dados = [str(input('Nome: ')), int(input('Peso: '))]
	pessoas.append(dados[:])
	
	if dados[1] > maior:
		maior = dados[1]

	if dados[1] < menor:
		menor = dados[1]
		
	dados.clear()
	
	continuar = ' '
	while continuar not in 'SN':
		continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	
	if continuar == 'N':
		break

print(f'Ao todo, você digitou {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}. Peso de', end=' ')

for lista in range(0, len(pessoas)-1):
	if pessoas[lista][1] == maior:
		print(pessoas[lista][0], end=' ')

print(f'\nO menor peso foi {menor}. Peso de', end=' ')

for lista in range(0, len(pessoas)-1):
	if pessoas[lista][1] == menor:
		print(pessoas[lista][0], end=' ')

