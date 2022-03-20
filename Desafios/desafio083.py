lista = []
expre = str(input('Digite um expressão: ')); lista.append(expre)
par = 0
par2 = 0
for l in lista:
	for expre in l:
		if expre in '(':
			par += 1
		elif expre in ')':
			par2 += 1

if par == par2:
	print('Sua expressão e valída')
else:
	print('Sua expressão e inválida')

