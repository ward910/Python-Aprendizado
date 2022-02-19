num = [int(input('Digite um número na Posição 0: ')), 
	int(input('Digite um número na Posição 1: ')), 
	int(input('Digite um número na Posição 2: ')), 
	int(input('Digite um número na Posição 3: ')), 
	int(input('Digite um número na Posição 4: '))]

print('=-'*30)
print('Você digitou os valores', num)

maior = max(num)
menor = min(num)
indexsMaior = []
indexsMenor = []

for n in num:
	if maior in num:
		index = num.index(maior)
		indexsMaior.append(index)
		num.remove(maior); num.insert(index, '0')

	if menor in num:
		index = num.index(menor)
		indexsMenor.append(index)
		num.remove(menor); num.insert(index, '0')

	if maior not in num and menor not in num:
		break

print(f'O maior valor digitado {maior} foi nas posições {indexsMaior[0:]}')
print(f'O menor valor digitado {menor} foi nas posições {indexsMenor[0:]}')
