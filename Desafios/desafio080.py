lista = []

for c in range(0, 5):
	num = str(input('Digite um valor: '))
	if len(lista) == 0 or num > lista[-1]:
		lista.append(num)
		print('Adicionado no final da lista...')
	else:
		for pos in range(0, len(lista)):
			if num <= lista[pos]:
				lista.insert(pos, num)
				print(f'Adicionado na posiçãos {pos} da lista...')
				break

print('-=' * 30)
print(f'Os posições valores digitados em ordem foram {lista}')
