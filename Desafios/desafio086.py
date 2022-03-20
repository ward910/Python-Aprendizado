matriz = [[], [], []]

somaPar = 0
linha = 0
coluna = 0
while coluna != 3:
	num = int(input('Digite um valor para [{}, {}]: '.format(coluna, linha))); matriz[coluna].append(num)
	
	if num % 2 == 0:
		somaPar += num 

	if len(matriz[coluna]) == 3:
		coluna += 1
	
	if linha >= 2:
		linha = 0
	else: 
		linha += 1

print('-=' * 30)

for c in range(0, len(matriz)):
	for l in range(0, len(matriz[c])):
		print(f'[   {matriz[c][l]}   ]', end=' ')
		
		if l == 2:
			print('\n')
