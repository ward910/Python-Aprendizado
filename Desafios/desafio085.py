lista = [[], []]

for x in range(0, 7):
	num = int(input('Digite o {}° valor: '.format(x + 1)))
	
	if num % 2 == 0:
		lista[0].append(num)
	else:
		lista[1].append(num)

lista[0].sort(reverse=True)
lista[1].sort(reverse=True)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')
